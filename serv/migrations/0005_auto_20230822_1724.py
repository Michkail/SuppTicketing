# Generated by Django 3.2.5 on 2023-08-22 10:24

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0004_auto_20230822_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactleader',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
        migrations.AlterField(
            model_name='contactrelation',
            name='contact',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True),
        ),
    ]
