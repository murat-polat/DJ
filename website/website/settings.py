
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_@-xn4bux8g9c()p41xi9@fo7317q)$)ovn=@m^6zhzr-vp!z='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['dj.revelmyra.net']
CSRF_TRUSTED_ORIGINS = ['https://dj.revelmyra.net']

# Application definition

INSTALLED_APPS = [
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts.apps.AccountsConfig',
    "corsheaders",
    'allauth.socialaccount.providers.microsoft',
    'allauth.socialaccount.providers.openid',
    'allauth.socialaccount.providers.openid_connect',
    'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.gitlab',
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.zoom',
    'allauth.socialaccount.providers.okta',
    'allauth.socialaccount.providers.saml',
    'django.contrib.sites',
    'allauth.socialaccount.providers.dataporten',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

SITE_ID = 1
ROOT_URLCONF = 'website.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'website.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    #     'ENGINE': 'django.db.backends.postgresql',
    #     'NAME': '',
    #     'USER': '',
    #     'PASSWORD': '',
    #     'HOST': '',
    #     'PORT': '5432'
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Oslo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_ROOT= os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# uvicorn website.asgi:application --host 0.0.0.0:8005 --reload

LOGIN_REDIRECT_URL = 'dashboard'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = "0.0.0.0"
# EMAIL_HOST_USER = ""
# EMAIL_HOST_PASSWORD = ""
# # EMAIL_HOST = "smtp.revelmyra.net"
# EMAIL_PORT = 1025



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = '0.0.0.0'
EMAIL_PORT = 1025
EMAIL_USE_TLS = False
EMAIL_USE_SSL = False
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''


AUTHENTICATION_BACKENDS = [
   
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by email
    'allauth.account.auth_backends.AuthenticationBackend',
    
]


SOCIALACCOUNT_PROVIDERS = {
    "openid_connect": {
        "APPS": [
            {
                "provider_id": "keycloak",
                "name": "Keycloak",
                "client_id": "",
                "secret": "",
                "settings": {
                    "server_url": "https://domain.net/realms/newdj/.well-known/openid-configuration",
                },

            }
        ]
        
    },
    'google': {
        'APP': {
            'client_id': '',
            'secret': '',
            'key': ''
        },
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    },
        "saml": {
        # Here, each app represents the SAML provider configuration of one
        # organization.
        "APP": 
            {
                # Used for display purposes, e.g. over by: {% get_providers %}
                "name": "Acme Inc",

                # Accounts signed up via this provider will have their
                # `SocialAccount.provider` value set to this ID. The combination
                # of this value and the `uid` must be unique. The IdP entity ID is a
                # good choice for this.
                "provider_id": "urn:dev-123.us.auth0.com",

                # The organization slug is configured by setting the
                # `client_id` value. In this example, the SAML login URL is:
                #
                #     /accounts/saml/acme-inc/login/
                "client_id": "acme-inc",

                # The fields above are common `SocialApp` fields. For SAML,
                # additional configuration is needed, which is placed in
                # `SocialApp.settings`:
                "settings": {
                    # Mapping account attributes to upstream (IdP specific) attributes.
                    # If left empty, an attempt will be done to map the attributes using
                    # built-in defaults.
                    "attribute_mapping": {
                        "uid": "http://schemas.auth0.com/clientID",
                        "email_verified": "http://schemas.auth0.com/email_verified",
                        "email": "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress",
                    },
                    # The configuration of the IdP.
                    "idp": {
                        # The entity ID of the IdP is required.
                        "entity_id": "urn:dev-123.us.auth0.com",

                        # Then, you can either specify the IdP's metadata URL:
                        "metadata_url": "https://dev-123.us.auth0.com/samlp/metadata/456",

                        # Or, you can inline the IdP parameters here as follows:
                        "sso_url": "https://dev-123.us.auth0.com/samlp/456",
                        "slo_url": "https://dev-123.us.auth0.com/samlp/456",
                        "x509cert": """
-----BEGIN CERTIFICATE-----
MIIDHTCCAgWgAwIBAgIJLogff5x+S0BlMA0GCSqGSIb3DQEBCwUAMCwxKjAoBgNV
BAMTIWRldi1uYXAybWY1ZTFwMXR3Z2Rv................................
................................G7qmyqcXRaf9HAuL/MvWz6zd96Ay6WHM
pXk92/DyUV48JxK/Bl7Bj8qjl5w5R7Dwps6wj+69PIAg
-----END CERTIFICATE-----
""",
                    },
                }
            }}
}
 