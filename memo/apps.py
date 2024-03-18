from django.apps import AppConfig

# class YourAppConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'memo'  # Replace 'your_app' with the actual name of your Django app

#     def ready(self):
#         import memo.cleanup_script  # Replace 'your_app' with the actual name of your Django app


class MemoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "memo"
