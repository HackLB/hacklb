"""
Application settings for HackLB project.
"""

# --------------------------------------------------
# Apps-related settings
# --------------------------------------------------

INSTALLED_APPS = []


# --------------------------------------------------
# Core apps are provided by Django
# --------------------------------------------------

CORE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
]
INSTALLED_APPS += CORE_APPS


# --------------------------------------------------
# Third-party apps are installed via pip
# --------------------------------------------------

ADDED_APPS = [
    'django_extensions',
    'haystack',
    'rest_framework',
    'rest_framework_gis',
    'bootstrap_pagination',
    'corsheaders',
]
INSTALLED_APPS += ADDED_APPS


# --------------------------------------------------
# Custom apps are unique to this project
# --------------------------------------------------

CUSTOM_APPS = [
    'core',
    'business',
    'crime',
    'geographic',
    'legistar',
]
INSTALLED_APPS += CUSTOM_APPS