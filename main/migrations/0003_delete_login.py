# Generated by Django 3.2.5 on 2022-10-17 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_user_login_username'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login',
        ),
    ]
