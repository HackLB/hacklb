"""
Database settings for HackLB project.
"""

# --------------------------------------------------
# Database settings
# --------------------------------------------------


if DEBUG:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": PROJECT_NAME,
            "USER": 'rogerhoward',
            "PASSWORD": "",
            "HOST": "localhost",
            "PORT": "",
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "parts",
            "USER": "django",
            "PASSWORD": "django102938",
            "HOST": "localhost",
            "PORT": "",
        }
    }