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
    bw_harvester=ckanext.offenedaten.harvesters.odm_harvesters:baden_wuerttemberg
    """,
)
