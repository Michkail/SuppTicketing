# Generated by Django 3.2.5 on 2023-10-20 07:31

import django.core.validators
from django.db import migrations, models
import serv.models


class Migration(migrations.Migration):

    dependencies = [
        ('serv', '0008_auto_20231017_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='id',
            field=models.CharField(editable=False, max_length=50, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='media_nd',
            field=models.FileField(blank=True, default=None, null=True, upload_to=serv.models.generate_unique_media_filename, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'mov', 'avi'])]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='media_rd',
            field=models.FileField(blank=True, default=None, null=True, upload_to=serv.models.generate_unique_media_filename, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'mov', 'avi'])]),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='media_st',
            field=models.FileField(blank=True, default=None, null=True, upload_to=serv.models.generate_unique_media_filename, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png', 'mp4', 'mov', 'avi'])]),
        ),
    ]
