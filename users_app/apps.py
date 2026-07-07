from django.apps import AppConfig


class UsersAppConfig(AppConfig):
    name = 'users_app'
    default_auto_field = 'django.db.models.BigAutoField'
    verbose_name = 'Пользователи'


    def ready(self):
        # Импортируем модуль сигналов внутри метода ready
        import users_app.signals # noqa: F401
