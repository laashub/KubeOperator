# Generated by Django 2.1.2 on 2019-06-10 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openshift_api', '0025_package_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='package',
            name='logo',
        ),
    ]