#coding: utf-8
import logging
import json

from ckan import model
from ckan.model import Session
from ckan.logic.action.update import package_update_rest

from ckanext.harvest.harvesters.ckanharvester import CKANHarvester

log = logging.getLogger(__name__)

EXCLUDE_OPEN_LICENSES = ['dl-de-by-1.0']


class OpenCKANHarvester(CKANHarvester):

    _groups_cache = {}

    def info(self):
        return {
            'name': 'ckan_open',
            'title': 'CKAN (Open)',
            'description': 'CKAN Harvester that only harvests datasets with open licenses.',
            'form_config_interface': 'Text'
        }

    def import_stage(self, harvest_object):
        package_dict = json.loads(harvest_object.content)

        # do not import packages that are not defined as open
        if not package_dict['isopen']:
            return

        if package_dict['license_id'] in EXCLUDE_OPEN_LICENSES:
            return

        super(OpenCKANHarvester, self).import_stage(harvest_object)

        if harvest_object.package_id:
            # Add some extras to the newly created package
            new_extras = {
                'harvest_catalogue_name': self.config.get('harvest_catalogue_name', ''),
                'harvest_catalogue_url': harvest_object.job.source.url,
                'harvest_dataset_url': harvest_object.job.source.url.strip('/') + '/package/' + harvest_object.package_id
            }

            context = {
                'model': model,
                'session': Session,
                'user': u'harvest',
                'id': harvest_object.package_id
            }

            data_dict = {'extras': new_extras}
            package_update_rest(data_dict, context)
