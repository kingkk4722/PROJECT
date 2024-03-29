# Generated by Django 5.0 on 2024-01-05 21:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ownership_transfer', '0014_ownershiptransfer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ownershiptransfer',
            name='new_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='new_owner', to='ownership_transfer.userprofile'),
        ),
        migrations.AlterField(
            model_name='ownershiptransfer',
            name='old_owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='old_owner', to='ownership_transfer.userprofile'),
        ),
    ]
