from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app.Authentication'

    def ready(self):
        import app.Authentication.signals
