from django.apps import AppConfig


class AppConfig(AppConfig):
    # id会自动创建
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
