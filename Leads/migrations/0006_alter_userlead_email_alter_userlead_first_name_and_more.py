# Generated by Django 4.1.1 on 2022-09-09 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0005_userlead_profile_lead'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlead',
            name='email',
            field=models.EmailField(max_length=150),
        ),
        migrations.AlterField(
            model_name='userlead',
            name='first_name',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='userlead',
            name='last_name',
            field=models.CharField(max_length=150),
        ),
    ]