"""Configuration for production mode."""

from .base import *  # noqa F403 enable * import for settings

DEBUG = False

ALLOWED_HOSTS = ["acme.com"]
