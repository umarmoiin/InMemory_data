# Generated by Django 4.2.5 on 2024-02-20 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("memo", "0004_rename_user_input_task_key_input_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task", old_name="key_input", new_name="key",
        ),
        migrations.RenameField(
            model_name="task", old_name="value_input", new_name="value",
        ),
    ]
