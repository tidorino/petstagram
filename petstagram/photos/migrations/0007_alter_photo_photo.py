# Generated by Django 4.1.5 on 2023-01-31 14:55

import cloudinary.models
from django.db import migrations
import petstagram.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0006_photo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, validators=[petstagram.core.validators.validate_max_image_size]),
        ),
    ]
