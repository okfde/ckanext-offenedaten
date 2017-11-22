import os
import re
import collections

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckan.common import OrderedDict


class UnexpectedDateFormat(Exception):
    pass


class OffeneDatenCustomizations(plugins.SingletonPlugin):
    plugins.implements(plugins.IRoutes)
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IFacets)

    def before_index(self, dataset_dict):

        # Change the Data Publica harvester's '2010-07-19T13:36:00'-formatted
        # date strings into SOLR-compatible '1995-12-31T23:59:59Z' ones.
        publica_format = ('^(?P<year>\d\d\d\d)-(?P<month>\d\d)-(?P<day>\d\d)'
                       'T(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>\d\d)$')

        solr_format = ('^(?P<year>\d\d\d\d)-(?P<month>\d\d)-(?P<day>\d\d)'
                      'T(?P<hours>\d\d):(?P<minutes>\d\d):(?P<seconds>\d\d)Z$')

        new_format = '{year}-{month}-{day}T{hours}:{minutes}:{seconds}Z'

        for date_key in ('deposit_date', 'update_date'):
            if date_key in dataset_dict.keys():
                match = re.match(publica_format, dataset_dict[date_key])
                if match:
                    solrfied_date = new_format.format(**match.groupdict())
                    dataset_dict[date_key] = solrfied_date
                elif re.match(solr_format, dataset_dict[date_key]):
                    # TODO: dates already appeared solrfied, if this is not
                    # needed in ckan2.0 we might be able to remove this
                    # code entirely
                    continue
                else:
                    raise UnexpectedDateFormat("{0} is not in Data Publica or"
                        " Solr Format for package {1}".format(date_key,
                                                        dataset_dict['id']))

        return dataset_dict

    def update_config(self, config):
        here = os.path.dirname(__file__)
        rootdir = os.path.dirname(os.path.dirname(here))

        our_public_dir = os.path.join(rootdir, 'ckanext', 'offenedaten', 'theme',
                'public')
        template_dir = os.path.join(rootdir, 'ckanext', 'offenedaten', 'theme',
                'templates')
        config['extra_public_paths'] = ','.join([our_public_dir,
                config.get('extra_public_paths', '')])
        config['extra_template_paths'] = ','.join([template_dir,
                config.get('extra_template_paths', '')])
        config['ckan.site_logo'] = ''
        config['ckan.site_title'] = 'OffeneDaten.de'
        config['ckan.favicon'] = '/images/favicon.ico'

        config['package_hide_extras'] = ' '.join(['harvest_catalogue_name',
                    'harvest_catalogue_url', 'harvest_dataset_url'])

        toolkit.add_resource('theme/fanstatic_library', 'ckanext-offenedaten')

    def dataset_facets(self, facets_dict, package_type):
        new_facets_dict = OrderedDict()
        new_facets_dict['openstatus'] = toolkit._('Offenheit')
        new_facets_dict['metadata_source_type'] = toolkit._('Source')
        #del facets_dict['tags']
        for key in facets_dict:
            new_facets_dict[key] = facets_dict[key]
        return new_facets_dict

    def group_facets(self, facets_dict, group_type, package_type):
        return self.dataset_facets(facets_dict, package_type)

    def organization_facets(self, facets_dict, organization_type, package_type):
        return self.dataset_facets(facets_dict, package_type)

    def before_map(self, route_map):
        wire_controller = 'ckanext.offenedaten.controllers:RewiringController'
        route_map.connect('/tag/{tags}', controller=wire_controller,
                          action='tag')

        subscribe_controller = 'ckanext.offenedaten.controllers:SubscribeController'
        route_map.connect('/subscribe',
                          controller=subscribe_controller,
                          conditions=dict(method=['POST']),
                          action='send')

        map_controller = 'ckanext.offenedaten.controllers:MapController'
        route_map.connect('/map', controller=map_controller, action='show')
        route_map.connect('/map/data.json', controller=map_controller,
                          action='data')

        return route_map

    def after_map(self, route_map):
        return route_map

    def read(self, pkg):
        try:
            toolkit.c.eu_country = pkg.extras.get('eu_country')
            if 'harvest_catalogue_name' in pkg.extras:
                toolkit.c.harvest_catalogue_name = pkg.extras[
                      'harvest_catalogue_name']
            if 'harvest_catalogue_url' in pkg.extras:
                toolkit.c.harvest_catalogue_url = pkg.extras[
                        'harvest_catalogue_url']
            if 'harvest_dataset_url' in pkg.extras:
                toolkit.c.harvest_dataset_url = pkg.extras[
                        'harvest_dataset_url']
        except TypeError:
            # FIXME: Why are we silencing TypeError here?
            pass
