""" User app cnfiguration """

from django.apps import AppConfig


class UsersConfig(AppConfig):
    """User Config
    """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'users'
