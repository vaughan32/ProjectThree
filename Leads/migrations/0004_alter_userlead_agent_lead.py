# Generated by Django 4.1.1 on 2022-09-09 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Leads', '0003_user_is_agent_user_is_orgarnizer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userlead',
            name='agent_lead',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Leads.useragent'),
        ),
    ]
