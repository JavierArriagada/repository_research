# Generated by Django 3.2.4 on 2021-06-30 16:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='thread',
            old_name='user',
            new_name='users',
        ),
    ]