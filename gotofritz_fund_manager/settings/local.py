"""Configuration for local development mode."""

from .base import *  # noqa F403 enable * import for settings

DEBUG = True

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]
