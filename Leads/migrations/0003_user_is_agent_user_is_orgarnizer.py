# Generated by Django 4.1.1 on 2022-09-09 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0002_userprofile_useragent_profile_agent'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_agent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_orgarnizer',
            field=models.BooleanField(default=True),
        ),
    ]
