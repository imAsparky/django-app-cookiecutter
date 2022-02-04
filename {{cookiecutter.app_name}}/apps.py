"""{{cookiecutter.app_name}} Apps file."""

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class AppNameConfig(AppConfig):
    """{{cookiecutter.app_name}} App name config."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "update_name"
    verbose_name = _("update_verbose_name")
    verbose_name_plural = _("update_verbose_plural_name")
