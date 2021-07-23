# Generated by Django 3.2.5 on 2021-07-22 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_auto_20210720_1540'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='cover',
        ),
        migrations.AlterField(
            model_name='page',
            name='pdf',
            field=models.FileField(max_length=200, upload_to='pages/pdfs/'),
        ),
    ]
