# from django.core.management.base import BaseCommand
# from django.conf import settings
# from memo.models import Task  # Replace 'your_app' with the actual name of your app

# class Command(BaseCommand):
#     help = 'Save temporary data to the database'

#     def handle(self, *args, **options):
#         temporary_data = getattr(settings, 'TEMPORARY_DATA', None)

#         if temporary_data:
#             user_input = temporary_data.get('user_input', '')
#             user_input2 = temporary_data.get('user_input2', '')

#             Task.objects.create(user_input=user_input, user_input2=user_input2)
#             self.stdout.write(self.style.SUCCESS('Temporary data saved to the database'))
#         else:
#             self.stdout.write(self.style.SUCCESS('No temporary data to save'))
