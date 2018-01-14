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
        'ndg-httpsclient',
        'requests[security]'
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
    krefeld_harvester=ckanext.offenedaten.harvesters.odm_harvesters:krefeld
    stadtbottrop_harvester=ckanext.offenedaten.harvesters.odm_harvesters:stadtbottrop
    stadtgeldern_harvester=ckanext.offenedaten.harvesters.odm_harvesters:stadtgeldern
    stadtkleve_harvester=ckanext.offenedaten.harvesters.odm_harvesters:stadtkleve
    stadtwesel_harvester=ckanext.offenedaten.harvesters.odm_harvesters:stadtwesel
    kreiswesel_harvester=ckanext.offenedaten.harvesters.odm_harvesters:kreiswesel
    kreisviersen_harvester=ckanext.offenedaten.harvesters.odm_harvesters:kreisviersen
    kreiskleve_harvester=ckanext.offenedaten.harvesters.odm_harvesters:kreiskleve
    gemeindewachtendonk_harvester=ckanext.offenedaten.harvesters.odm_harvesters:gemeindewachtendonk
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
    meerbusch_harvester=ckanext.offenedaten.harvesters.odm_harvesters:meerbusch
    gelsenkirchen_harvester=ckanext.offenedaten.harvesters.odm_harvesters:gelsenkirchen
    duesseldorf_harvester=ckanext.offenedaten.harvesters.odm_harvesters:duesseldorf
    wuppertal_harvester=ckanext.offenedaten.harvesters.odm_harvesters:wuppertal
    muelheim_ruhr_harvester=ckanext.offenedaten.harvesters.odm_harvesters:muelheim_ruhr
    leipzig_harvester=ckanext.offenedaten.harvesters.odm_harvesters:leipzig
    kerpen_harvester=ckanext.offenedaten.harvesters.odm_harvesters:kerpen
    bergheim_harvester=ckanext.offenedaten.harvesters.odm_harvesters:bergheim
    bruehl_harvester=ckanext.offenedaten.harvesters.odm_harvesters:bruehl
    kall_harvester=ckanext.offenedaten.harvesters.odm_harvesters:kall
    elsdorf_harvester=ckanext.offenedaten.harvesters.odm_harvesters:elsdorf
    euskirchen_harvester=ckanext.offenedaten.harvesters.odm_harvesters:euskirchen
    merzenich_harvester=ckanext.offenedaten.harvesters.odm_harvesters:merzenich
    juelich_harvester=ckanext.offenedaten.harvesters.odm_harvesters:juelich
    huertgenwald_harvester=ckanext.offenedaten.harvesters.odm_harvesters:huertgenwald
    langerwehe_harvester=ckanext.offenedaten.harvesters.odm_harvesters:langerwehe
    wesseling_harvester=ckanext.offenedaten.harvesters.odm_harvesters:wesseling
    vettweiss_harvester=ckanext.offenedaten.harvesters.odm_harvesters:vettweiss
    heimbach_harvester=ckanext.offenedaten.harvesters.odm_harvesters:heimbach
    kreuzau_harvester=ckanext.offenedaten.harvesters.odm_harvesters:kreuzau
    linnich_harvester=ckanext.offenedaten.harvesters.odm_harvesters:linnich
    bad_muenstereifel_harvester=ckanext.offenedaten.harvesters.odm_harvesters:bad_muenstereifel
    titz_harvester=ckanext.offenedaten.harvesters.odm_harvesters:titz
    bedburg_harvester=ckanext.offenedaten.harvesters.odm_harvesters:bedburg
    noervenich_harvester=ckanext.offenedaten.harvesters.odm_harvesters:noervenich
    niederzier_harvester=ckanext.offenedaten.harvesters.odm_harvesters:niederzier
    """,
)
