# Generated by Django 5.1.6 on 2025-06-06 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alertSystem', '0002_alter_alert_isactive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='alertTimestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
