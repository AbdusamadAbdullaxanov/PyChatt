# Generated by Django 4.1.3 on 2022-11-26 16:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UsersAuthentication', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUserModel',
        ),
    ]