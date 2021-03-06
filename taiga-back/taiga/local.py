# -*- coding: utf-8 -*-
# Copyright (C) 2014-2017 Andrey Antukh <niwi@niwi.nz>
# Copyright (C) 2014-2017 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014-2017 David Barragán <bameda@dbarragan.com>
# Copyright (C) 2014-2017 Alejandro Alonso <alejandro.alonso@kaleidos.net>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .common import *

#########################################
## GENERIC
#########################################

DEBUG = (os.getenv("DEBUG", "False") == "True")
SECRET_KEY = os.getenv("SECRET_KEY")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "HOST": os.getenv("DB_HOST", "localhost"),
        "PORT": os.getenv("DB_PORT", "5432"),
        "NAME": os.getenv("DB_NAME", "taiga"),
        "USER": os.getenv("DB_USER", "postgres"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
    }
}

SITES = {
    "api": {
        "scheme": os.getenv("API_PUBLIC_PROTOCOL", "http"),
        "domain": os.getenv("API_PUBLIC_DOMAIN", "localhost:8000"),
        "name": "api"
    },
    "front": {
        "scheme": os.getenv("FRONTEND_PUBLIC_PROTOCOL", "http"),
        "domain": os.getenv("FRONTEND_PUBLIC_DOMAIN", "localhost:8000"),
        "name": "front"
    },
}

MEDIA_URL = os.getenv("MEDIA_URL", "http://localhost:8000/media/")
STATIC_URL = os.getenv("STATIC_URL", "http://localhost:8000/static/")

#########################################
## THROTTLING
#########################################

# REST_FRAMEWORK["DEFAULT_THROTTLE_RATES"] = {
#    "anon-write": "20/min",
#    "user-write": None,
#    "anon-read": None,
#    "user-read": None,
#    "import-mode": None,
#    "import-dump-mode": "1/minute",
#    "create-memberships": None,
#    "login-fail": None,
#    "register-success": None,
#    "user-detail": None,
#    "user-update": None,
# }

# This list should contain:
#  - Taiga users IDs
#  - Valid clients IP addresses (X-Forwarded-For header)
# REST_FRAMEWORK["DEFAULT_THROTTLE_WHITELIST"] = []


#########################################
## MAIL SYSTEM SETTINGS
#########################################

DEFAULT_FROM_EMAIL = os.getenv("DEFAULT_FROM_EMAIL")
CHANGE_NOTIFICATIONS_MIN_INTERVAL = 300  # seconds

# EMAIL SETTINGS EXAMPLE
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = (os.getenv("EMAIL_USE_TLS", "True") == "True")  # convert to boolean
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = os.getenv("EMAIL_PORT")
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD")

# GMAIL SETTINGS EXAMPLE
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_USE_TLS = True
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'youremail@gmail.com'
# EMAIL_HOST_PASSWORD = 'yourpassword'


#########################################
## REGISTRATION
#########################################

PUBLIC_REGISTER_ENABLED = (os.getenv("PUBLIC_REGISTER_ENABLED", "False") == "True")  # convert to boolean

# LIMIT ALLOWED DOMAINS FOR REGISTER AND INVITE
# None or [] values in USER_EMAIL_ALLOWED_DOMAINS means allow any domain
# USER_EMAIL_ALLOWED_DOMAINS = None

# PUBLIC OR PRIVATE NUMBER OF PROJECT PER USER
# MAX_PRIVATE_PROJECTS_PER_USER = None # None == no limit
# MAX_PUBLIC_PROJECTS_PER_USER = None # None == no limit
# MAX_MEMBERSHIPS_PRIVATE_PROJECTS = None # None == no limit
# MAX_MEMBERSHIPS_PUBLIC_PROJECTS = None # None == no limit

# GITHUB SETTINGS
# GITHUB_URL = "https://github.com/"
# GITHUB_API_URL = "https://api.github.com/"
# GITHUB_API_CLIENT_ID = "yourgithubclientid"
# GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"


#########################################
## SITEMAP
#########################################

# If is True /front/sitemap.xml show a valid sitemap of taiga-front client
# FRONT_SITEMAP_ENABLED = False
# FRONT_SITEMAP_CACHE_TIMEOUT = 24*60*60  # In second


#########################################
## FEEDBACK
#########################################

# Note: See config in taiga-front too
# FEEDBACK_ENABLED = True
# FEEDBACK_EMAIL = "support@taiga.io"


#########################################
## STATS
#########################################

STATS_ENABLED = (os.getenv("STATS_ENABLED", "True") == "True")  # convert to boolean
# FRONT_SITEMAP_CACHE_TIMEOUT = 60*60  # In second


#########################################
## CELERY
#########################################
# Set to True to enable celery and work in async mode or False
# to disable it and work in sync mode. You can find the celery
# settings in settings/celery.py and settings/celery-local.py
# CELERY_ENABLED = True


#########################################
## IMPORTERS
#########################################

# Configuration for the GitHub importer
# Remember to enable it in the front client too.
# IMPORTERS["github"] = {
#    "active": True, # Enable or disable the importer
#    "client_id": "XXXXXX_get_a_valid_client_id_from_github_XXXXXX",
#    "client_secret": "XXXXXX_get_a_valid_client_secret_from_github_XXXXXX"
# }

# Configuration for the Trello importer
# Remember to enable it in the front client too.
# IMPORTERS["trello"] = {
#    "active": True, # Enable or disable the importer
#    "api_key": "XXXXXX_get_a_valid_api_key_from_trello_XXXXXX",
#    "secret_key": "XXXXXX_get_a_valid_secret_key_from_trello_XXXXXX"
# }

# Configuration for the Jira importer
# Remember to enable it in the front client too.
IMPORTERS["jira"] = {
    "active": (os.getenv("JIRA_IMPORTER_ACTIVE", "False") == "True"),  # Convert to boolean
    "consumer_key": os.getenv("JIRA_CONSUMER_KEY"),
    "cert": os.getenv("JIRA_PRIVATE_CERT"),
    "pub_cert": os.getenv("JIRA_PUBLIC_CERT")
}

# Configuration for the Asane importer
# Remember to enable it in the front client too.
# IMPORTERS["asana"] = {
#    "active": True, # Enable or disable the importer
#    "callback_url": "{}://{}/project/new/import/asana".format(SITES["front"]["scheme"],
#                                                              SITES["front"]["domain"]),
#    "app_id": "XXXXXX_get_a_valid_app_id_from_asana_XXXXXX",
#    "app_secret": "XXXXXX_get_a_valid_app_secret_from_asana_XXXXXX"
# }
