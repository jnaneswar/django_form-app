# Generated by Django 2.2.2 on 2019-06-09 10:35

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20190609_1600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=phone_field.models.PhoneField(max_length=10),
        ),
    ]
