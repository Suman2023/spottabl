# Generated by Django 4.0.4 on 2022-05-11 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientUserInvite',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('client_code', models.CharField(max_length=30)),
                ('user_type', models.CharField(max_length=30)),
                ('accepted', models.BooleanField(default=False)),
                ('role', models.CharField(max_length=30)),
                ('inviter', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('enabled', models.BooleanField(default=False)),
                ('registration_type', models.CharField(max_length=30)),
                ('user_type', models.CharField(max_length=30)),
            ],
        ),
    ]
