# Generated by Django 4.1.1 on 2022-09-11 05:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0008_remove_city_state'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessdetails',
            name='state',
        ),
    ]
