# ckanext-offenedaten

Custom CKAN extension for [offenedaten.de](http://offenedaten.de/)

## How to Install Locally for Development

1. Install CKAN from source.

2. Install ckanext-offenedaten. Activate your CKAN virtual environment and:

        git clone git@github.com:okfn/ckanext-offenedaten.git
        cd ckanext-offenedaten
        python setup.py develop
        pip install -r pip-requirements.txt

3. Add the following settings to the `[app:main]` section of your CKAN config
   file (e.g. `development.ini` or `offenedaten.ini`):

        offenedaten.beta = true

   and edit the following settings:

        ckan.plugins = stats dcat_api offenedaten
        ckan.site_title = offenedaten.de
        ckan.site_description = Open Data Repository

4. Run CKAN, e.g. `paster serve offenedaten.ini`

Note on CKAN versions: at the time of writing the `master` branch of
ckanext-offenedaten is intended to work with CKAN 2.0 (currently the `master` branch
of ckan).
