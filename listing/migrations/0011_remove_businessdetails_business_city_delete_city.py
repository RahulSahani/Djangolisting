# Generated by Django 4.1.1 on 2022-09-11 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0010_rename_city_businessdetails_business_city_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businessdetails',
            name='business_city',
        ),
        migrations.DeleteModel(
            name='City',
        ),
    ]
