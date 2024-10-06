from django.apps import AppConfig


class SignalAssignmentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signal_assignment'
    def ready(self) -> None:
        import signal_assignment.models
