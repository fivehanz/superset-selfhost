import os

# Get Redis host and port from environment variables
REDIS_HOST = os.getenv('REDIS_HOST', 'redis')
REDIS_PORT = os.getenv('REDIS_PORT', '6379')


from flask_talisman import Talisman

TALISMAN_ENABLED = False

# TALISMAN_CONFIG = {
#     'content_security_policy': {
#         'default-src': '\'self\'',
#         'script-src': '\'self\'',
#         'style-src': '\'self\'',
#         'img-src': '\'self\' data:'
#     },
#     'content_security_policy_nonce_in': ['script-src']
# }

CONTENT_SECURITY_POLICY_WARNING = False

RATELIMIT_ENABLED = True
RATELIMIT_STORAGE_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/3'

