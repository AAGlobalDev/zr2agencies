# Generated by Django 3.0.3 on 2020-02-20 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='portfolio_site',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='profile_pic',
        ),
    ]
