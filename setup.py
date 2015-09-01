import setuptools

version = '0.1'

setuptools.setup(
    name='ckanext-offenedaten',
    version=version,
    description="CKAN extension for offenedaten.de",
    long_description="""\
    """,
    # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[],
    keywords='',
    author='okfn',
    author_email='info@okfn.org',
    url='',
    license='',
    packages=setuptools.find_packages(
        exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.offenedaten'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points="""
        [ckan.plugins]
    # Add plugins here
    offenedaten=ckanext.offenedaten.plugin:OffeneDatenCustomizations
    open_ckan_harvester=ckanext.offenedaten.harvesters:OpenCKANHarvester
    arnsberg_harvester=ckanext.offenedaten.harvesters.odm_harvesters:arnsberg
    bw_harvester=ckanext.offenedaten.harvesters.odm_harvesters:baden_wuerttemberg
    bayern_harvester=ckanext.offenedaten.harvesters.odm_harvesters:bayern
    bochum_harvester=ckanext.offenedaten.harvesters.odm_harvesters:bochum
    braunschweig_harvester=ckanext.offenedaten.harvesters.odm_harvesters:braunschweig
    bremen_harvester=ckanext.offenedaten.harvesters.odm_harvesters:bremen
    diepholz_harvester=ckanext.offenedaten.harvesters.odm_harvesters:diepholz
    moers_harvester=ckanext.offenedaten.harvesters.odm_harvesters:moers
    rostock_harvester=ckanext.offenedaten.harvesters.odm_harvesters:rostock
    rlp_harvester=ckanext.offenedaten.harvesters.odm_harvesters:rheinland_pfalz
    ulm_harvester=ckanext.offenedaten.harvesters.odm_harvesters:ulm
    koeln_harvester=ckanext.offenedaten.harvesters.odm_harvesters:koeln
    aachen_harvester=ckanext.offenedaten.harvesters.odm_harvesters:aachen
    hamburg_harvester=ckanext.offenedaten.harvesters.odm_harvesters:hamburg
    frankfurt_harvester=ckanext.offenedaten.harvesters.odm_harvesters:frankfurt
    berlin_harvester=ckanext.offenedaten.harvesters.odm_harvesters:berlin
    bonn_harvester=ckanext.offenedaten.harvesters.odm_harvesters:bonn
    muenchen_harvester=ckanext.offenedaten.harvesters.odm_harvesters:muenchen
    """,
)
