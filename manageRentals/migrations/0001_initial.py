# Generated by Django 5.1.6 on 2025-06-05 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rental',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('isbn', models.IntegerField(max_length=13)),
                ('issuerId', models.IntegerField(max_length=10)),
                ('userId', models.IntegerField(max_length=15)),
                ('rentDate', models.DateTimeField(auto_now=True)),
                ('returnDate', models.DateTimeField()),
                ('isActive', models.BooleanField()),
            ],
        ),
    ]
