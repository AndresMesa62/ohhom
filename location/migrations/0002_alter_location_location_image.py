# Generated by Django 4.1.6 on 2023-03-21 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("location", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="location",
            name="location_Image",
            field=models.ImageField(upload_to="photos/locations"),
        ),
    ]
