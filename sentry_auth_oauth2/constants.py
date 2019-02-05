from __future__ import absolute_import, print_function

from django.conf import settings

CLIENT_ID = getattr(settings, 'OAUTH2_APP_ID', None)

CLIENT_SECRET = getattr(settings, 'OAUTH2_API_SECRET', None)

REQUIRE_VERIFIED_EMAIL = getattr(settings, 'OAUTH2_REQUIRE_VERIFIED_EMAIL', False)

ERR_NO_ORG_ACCESS = 'You do not have access to the required Generic organization.'

ERR_NO_PRIMARY_EMAIL = 'We were unable to find a primary email address associated with your Generic acount.'

ERR_NO_SINGLE_PRIMARY_EMAIL = 'We were unable to find a single primary email address associated with your Generic acount.'

ERR_NO_VERIFIED_PRIMARY_EMAIL = 'We were unable to find a verified, primary email address associated with your Generic acount.'

ERR_NO_SINGLE_VERIFIED_PRIMARY_EMAIL = 'We were unable to find a single verified, primary email address associated with your Generic acount.'

# we request repo as we share scopes with the other Generic integration
SCOPE = 'user:email,read:org,repo'

# deprecated please use OAUTH2_API_DOMAIN and GITHUB_BASE_DOMAIN
DOMAIN = getattr(settings, 'OAUTH2_DOMAIN', 'api.oauth2.com')

BASE_DOMAIN = getattr(settings, 'OAUTH2_BASE_DOMAIN', 'oauth2.com')
API_DOMAIN = getattr(settings, 'OAUTH2_API_DOMAIN', DOMAIN)

ACCESS_TOKEN_URL = 'https://{0}/oauth/access_token'.format(BASE_DOMAIN)
AUTHORIZE_URL = 'https://{0}/oauth/authorize'.format(BASE_DOMAIN)
