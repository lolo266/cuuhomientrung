# Generated by Django 3.1 on 2020-10-12 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_auto_20201012_1745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='youtubeclip',
            old_name='bad_topic',
            new_name='topic',
        ),
    ]
