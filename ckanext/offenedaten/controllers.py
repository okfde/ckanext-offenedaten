from pylons.i18n import _
import os

from sqlalchemy import distinct, func
from urllib import urlencode

from ckan.common import OrderedDict

import ckan.plugins as p
import ckan.lib.helpers as h

from ckan.lib.helpers import json
from ckan.lib.base import BaseController, c, g, request, \
                          response, render, config, abort, redirect
                          
from ckan import model
from ckan.model import Session, PackageExtra, Package, Group
import ckan.logic as logic
import ckan.lib.maintain as maintain

import ckan.lib.plugins

import logging
log = logging.getLogger(__name__)

from datetime import datetime

get_action = logic.get_action
lookup_package_plugin = ckan.lib.plugins.lookup_package_plugin


def get_root_dir():
    here = os.path.dirname(__file__)
    rootdir = os.path.dirname(os.path.dirname(here))
    return rootdir


#class RewiringController(BaseController):
#
#    def tag(self, tags):
#        redirect(h.url_for(controller='package', action='search', tags=tags))

class MapController(BaseController):
    def _search_template(self, package_type):
        return lookup_package_plugin(package_type).search_template()

    def _compactresults(self, item):
        notinextras = ('name', 'title', 'package_count')
        inextras = ('url', 'latitude', 'longitude', 'polygon', 'city_type', 'contact_email', 'open_data_portal')
        ritem = {}
        for key in notinextras:
            ritem[key] = item[key]
        for key in inextras:
            if key in item['extras']:
                ritem[key] = item['extras'][key]
        return ritem  

    def _encode_params(self, params):
        return [(k, v.encode('utf-8') if isinstance(v, basestring) else str(v))
            for k, v in params]

    def url_with_params(self, url, params):
        params = self._encode_params(params)
        return url + u'?' + urlencode(params)
            
    def search_url(self, params, package_type=None):
        if not package_type or package_type == 'dataset':
            url = h.url_for(controller='package', action='search')
        else:
            url = h.url_for('{0}_search'.format(package_type))
        return self.url_with_params(url, params)
        
    def _setup_template_variables(self, context, data_dict, package_type=None):
        return lookup_package_plugin(package_type).\
            setup_template_variables(context, data_dict)

    def show(self):
        #This is based on the CKAN package search controller
        #There are probably still some pieces we don't need
        #And using the facets to get the info we need is not ideal
        #because normal facet limits are then not applied on the page
        from ckan.lib.search import SearchError

        # unicode format (decoded from utf8)
        q = c.q = request.params.get('q', u'')
        c.query_error = False

        def remove_field(key, value=None, replace=None):
            return h.remove_url_param(key, value=value, replace=replace,
                                  controller='package', action='search')

        c.remove_field = remove_field
        
        params_nopage = [(k, v) for k, v in request.params.items()]
        
        def pager_url(q=None, page=None):
            params = list(params_nopage)
            return self.search_url(params, 'dataset')
            
        c.search_url_params = urlencode(self._encode_params(params_nopage))

        try:
            c.fields = []
            # c.fields_grouped will contain a dict of params containing
            # a list of values eg {'tags':['tag1', 'tag2']}
            c.fields_grouped = {}
            search_extras = {}
            fq = ''
            for (param, value) in request.params.items():
                if param not in ['q', 'page', 'sort'] \
                        and len(value) and not param.startswith('_'):
                    if not param.startswith('ext_'):
                        c.fields.append((param, value))
                        fq += ' %s:"%s"' % (param, value)
                        if param not in c.fields_grouped:
                            c.fields_grouped[param] = [value]
                        else:
                            c.fields_grouped[param].append(value)
                    else:
                        search_extras[param] = value

            context = {'model': model, 'session': model.Session,
                       'user': c.user or c.author, 'for_view': True,
                       'auth_user_obj': c.userobj}

            facets = OrderedDict()

            default_facet_titles = {
                    'organization': _('Organizations'),
                    'groups': _('Groups'),
                    'tags': _('Tags'),
                    'res_format': _('Formats'),
                    'license_id': _('Licenses'),
                    }

            for facet in g.facets:
                if facet in default_facet_titles:
                    facets[facet] = default_facet_titles[facet]
                else:
                    facets[facet] = facet

            # Facet titles
            for plugin in p.PluginImplementations(p.IFacets):
                facets = plugin.dataset_facets(facets, 'dataset')

            c.facet_titles = facets

            #We use the organization facet to get the list of organizations detected for this query
            #The actual data is irrelevant
            data_dict = {
                'q': q,
                'fq': fq.strip(),
                'facet.field': facets.keys(),
                'facet.limit': -1,
                'extras': search_extras,
                'rows': 1
            }

            query = get_action('package_search')(context, data_dict)

            orglist = query['facets']['organization'].keys()
                
            #Now get the data concerning the orgs
            q = Session.query(Group).filter(Group.name.in_(orglist))
            
            values = []
            qres = q.all()

            #Combine in extras, add counts
            #Make the data look like what we get with a org search
            for d in qres:
                dobj = d.as_dict()
                dobj['extras'] = d.extras
                dobj['package_count'] = query['facets']['organization'][dobj['name']]
                values.append(dobj)

            c.page = h.Page(
                collection=query['results'],
                url=pager_url,
                item_count=query['count']
            )
            c.facets = query['facets']
            c.search_facets = query['search_facets']
            c.page.items = query['results']
        except SearchError, se:
            log.error('Dataset search (map) error: %r', se.args)
            c.query_error = True
            c.facets = {}
            c.search_facets = {}

        maintain.deprecate_context_item(
          'facets',
          'Use `c.search_facets` instead.')

        self._setup_template_variables(context, {},
                                       package_type='dataset')
                                       
        passresults = map(self._compactresults, values)
        c.results = json.dumps(passresults)
        '''
        return render(self._search_template('dataset'),
                      extra_vars={'dataset_type': 'dataset'})
        '''
        return render('home/map.html')     

    def data(self):
        # Get the Europe dataset
        rootdir = get_root_dir()
        data_file = os.path.join(rootdir, 'ckanext', 'offenedaten', 'data', 'eu.json')
        f = open(data_file, 'r')
        o = json.load(f)

        # Get the package count by country
        q = Session.query(
                distinct(PackageExtra.value),
                func.count(PackageExtra.value)
            ).\
                filter(PackageExtra.key == u'eu_country').\
                group_by(PackageExtra.value)

        values = dict(q.all())
        # Set the package count for each country
        
        for ft in o['features']:
            code = ft['properties']['NUTS']
            ft['properties']['packages'] = (values.get(code, 0))

        response.content_type = 'application/json'
        response.pragma = None
        response.cache_control = 'public; max-age: 3600'
        response.cache_expires(seconds=3600)
        return json.dumps(o)
