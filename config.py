import os

# The secret key is used by Flask to encrypt session cookies.
SECRET_KEY = 'secret'

# There are three different ways to store the data in the application.
# You can choose 'datastore', 'cloudsql', or 'mongodb'. Be sure to
# configure the respective settings for the one you choose below.
# You do not have to configure the other data backends. If unsure, choose
# 'datastore' as it does not require any additional configuration.
DATA_BACKEND = 'datastore'

# Google Cloud Project ID. This can be found on the 'Overview' page at
# https://console.developers.google.com
PROJECT_ID = 'soilgenerate'

# Google Cloud Storage and upload settings.
# Typically, you'll name your bucket the same as your project. To create a
# bucket:
#
#   $ gsutil mb gs://<your-bucket-name>
#
# You also need to make sure that the default ACL is set to public-read,
# otherwise users will not be able to see their upload images:
#
#   $ gsutil defacl set public-read gs://<your-bucket-name>
#
# You can adjust the max content length and allow extensions settings to allow
# larger or more varied file types if desired.
CLOUD_STORAGE_BUCKET = 'plant-data'
# MAX_CONTENT_LENGTH = 8 * 1024 * 1024
# ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

ARG_DATA = {'growth_rate': None, 'percip_max': 30, 'hardiness': -10, 'cn_target': 30, \
            'animal_browse': 'low-med-high', 'full_sun': False, 'full_shade': False, \
            'max_height': None, 'cn_ratio': 'low-med-high', 'known_supplier': False, \
            'area': 1200, 'budget': False, 'percip_min': 20, 'soil_texture': 'course', \
            'invasive': False}