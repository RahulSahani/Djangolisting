# Generated by Django 4.1.1 on 2022-09-11 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0009_remove_businessdetails_state'),
    ]

    operations = [
        migrations.RenameField(
            model_name='businessdetails',
            old_name='city',
            new_name='business_city',
        ),
        migrations.RemoveField(
            model_name='businessdetails',
            name='country',
        ),
    ]
