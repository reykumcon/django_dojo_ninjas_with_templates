# Generated by Django 2.2 on 2021-04-01 02:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dojo',
            old_name='start',
            new_name='state',
        ),
    ]
