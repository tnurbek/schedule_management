# Generated by Django 3.1.2 on 2020-11-11 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0004_scheduledoctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='duration',
            field=models.PositiveIntegerField(default=0),
        ),
    ]