# Generated by Django 4.1.6 on 2023-03-20 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Location",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("location_name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200, unique=True)),
                ("location_state", models.CharField(max_length=200)),
                ("location_country", models.CharField(max_length=200)),
                ("location_description", models.CharField(max_length=255)),
                ("location_Image", models.ImageField(upload_to="photos/locations/")),
            ],
        ),
    ]
