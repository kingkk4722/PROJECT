# Generated by Django 5.0 on 2024-01-03 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ownership_transfer', '0012_alter_ownership_user_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ownership',
            name='user_profile',
        ),
    ]
