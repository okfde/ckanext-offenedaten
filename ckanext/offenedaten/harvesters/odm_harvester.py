# coding: utf-8
import logging
from hashlib import sha1
import ckan.plugins as p
from ckan.lib.helpers import json
from ckanext.harvest.model import HarvestObject
from ckanext.harvest.harvesters import HarvesterBase
from ckan import model
from ckan.model import Session
from ckan.logic.action.create import organization_create

from odm.catalogs.utils import metautils

log = logging.getLogger(__name__)


class OdmHarvester(HarvesterBase):

    scraper = None

    def __init__(self, *args, **kwargs):
        self.config = {"user": "harvester"}

    def _set_config(self, config_str):
        self.api_key = None
        if config_str:
            self.config = json.loads(config_str)
            if 'api_version' in self.config:
                self.api_version = int(self.config['api_version'])
            if 'api_key' in self.config:
                self.api_key = self.config['api_key']
            log.debug('Using config: %r', self.config)
        else:
            self.config = {}

    def info(self):
        return self.scraper.info()

    def gather_stage(self, harvest_job):
        log.debug('In gather_stage of ' + self.info()['title'])
        self._set_config(harvest_job.source.config)
        ids = []
        
        if self.api_key !=  None:
            ds = self.scraper.gather(apikey = self.api_key)
        else:
            ds = self.scraper.gather()
        for d in ds:
            try:
                id = d.get('id', False)
                if not id:
                    id = sha1(d['url'].encode('utf-8')).hexdigest()
                d = json.dumps(d)
                obj = HarvestObject(guid=id, job=harvest_job, content=d)
                obj.save()
                ids.append(obj.id)
            except:
                print "error"
        return ids

    def fetch_stage(self, harvest_object):
        log.debug('In fetch_stage  ' + self.info()['title'])
        d = json.loads(harvest_object.content)
        d = self.scraper.fetch(d)
        harvest_object.content = json.dumps(d)
        harvest_object.save()
        return True

    def _open_to_string(self, open):
        if open is None:
            return 'Unbekannt'
        elif open:
            return 'Offen'
        else:
            return 'Nicht offen'
            
    def _create_unexisting_org(self, org_name):
        try:
            p.toolkit.get_action('organization_show')({}, {'id': org_name})

        except p.toolkit.ObjectNotFound:
            context = {"model": model, 'session': Session, 'user': self.config['user']}
            organization_create(context, {"name": org_name})

    def import_stage(self, harvest_object):
        log.debug('In import_stage of ' + self.info()['title'])
        if not harvest_object:
            log.error('No harvest object received')
            return False

        if harvest_object.content is None:
            self._save_object_error('Empty content for object %s' % harvest_object.id, harvest_object, 'Import')
            return False

        try:
            rec = json.loads(harvest_object.content)
            rec = self.scraper.import_data(rec)

            # snippet from odm-datenerfassung/utils/export_to_ckan.py
            d = {}
            #If the city field is not set, it should mean the whole thing is empty/not intended to be imported. All ODM data must be tied to a 'city'.
            if 'city' not in rec:
                return
            d['id'] = harvest_object.guid
            d['owner_org'] = rec['city']
            # TODO: issue a warning if the org does not exist yet (this shouldn't happen often)
            # self._create_unexisting_org(d['owner_org'])

            d['state'] = 'active' if rec['accepted'] else 'deleted'
            d['url'] = rec['url']
            d['title'] = rec['title']
            # d['name'] = str(uuid.uuid4()) #Must be unique, our titles are not
            d['name'] = self._gen_new_name(d['title'])
            d['notes'] = rec['description']
            metadata = rec['metadata']
            d['extras'] = { 'metadata_modified': metadata['metadata_modified'], 'metadata_created': metadata['metadata_created'], 'temporalextent': rec['temporalextent'], 'metadata_source_portal': rec['originating_portal'] }
            d['license_id'] = rec['licenseshort']
            d['isopen'] = rec['open']
            d['maintainer'] = rec['publisher']
            #N.B. groups have to be created, before they can be assigned
            #Groups are dictionaries. We use them via title which is what we store
            d['groups'] = map(metautils.force_alphanumeric_short, rec['categories'])
            d['resources'] = set()
            #Duplicates in resources not allowed. Actually we shouldn't allow them either...
            rurls = set()
            for url in rec['filelist']:
                rurls.add(url)
            d['resources'] = []
            for url in rurls:
                d['resources'].append({'url': url})
            log.debug('In Import state with object', d)
            return self._create_or_update_package(d, harvest_object)
            # return False # self._create_or_update_package(d, harvest_object)

        except Exception, e:
            log.exception(e)
            self._save_object_error('%r' % e, harvest_object, 'Import')

