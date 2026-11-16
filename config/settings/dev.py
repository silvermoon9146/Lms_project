from .base import *

DEBUG = config("D_DEBUG", cast=bool, default=True)
ALLOWED_HOSTS += ["127.0.0.1", "localhost"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config("D_NAME"),
        "USER": config("D_USER"),
        "PASSWORD": config("D_PASSWORD"),
        "HOST": config("D_HOST"),
        "PORT": config("D_PORT", cast=int),
    }
}
