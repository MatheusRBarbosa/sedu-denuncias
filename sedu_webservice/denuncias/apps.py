from django.apps import AppConfig


class DenunciasConfig(AppConfig):
    name = 'denuncias'
    def ready(self):
        import denuncias.signals
