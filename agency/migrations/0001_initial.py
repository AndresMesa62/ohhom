# Generated by Django 4.1.6 on 2023-02-09 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("category", "0003_alter_category_slug"),
    ]

    operations = [
        migrations.CreateModel(
            name="Property",
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
                ("property_name", models.CharField(max_length=200)),
                ("slug", models.SlugField(max_length=200)),
                ("description", models.TextField(blank=True, max_length=500)),
                ("price", models.IntegerField()),
                ("images", models.ImageField(upload_to="photos/properties")),
                ("created_date", models.DateTimeField(auto_now_add=True)),
                ("modified_date", models.DateTimeField(auto_now=True)),
                ("address", models.CharField(max_length=200)),
                ("municipality", models.CharField(max_length=200)),
                ("state", models.CharField(max_length=200)),
                ("country", models.CharField(max_length=200)),
                ("is_verified", models.BooleanField(default=False)),
                ("area", models.IntegerField()),
                ("rooms", models.IntegerField()),
                ("bathrooms", models.IntegerField()),
                ("dining_room", models.IntegerField()),
                ("floor", models.IntegerField()),
                ("is_avalible", models.BooleanField(default=True)),
                ("allows_pets", models.BooleanField(default=False)),
                ("allows_kids", models.BooleanField(default=False)),
                ("has_motorcycle_parking", models.BooleanField(default=False)),
                ("has_car_parking", models.BooleanField(default=False)),
                ("has_garden", models.BooleanField(default=False)),
                ("has_elevator", models.BooleanField(default=False)),
                ("has_security", models.BooleanField(default=False)),
                ("has_pool", models.BooleanField(default=False)),
                ("has_gym", models.BooleanField(default=False)),
                ("has_integral_kitchen", models.BooleanField(default=False)),
                ("has_closets", models.BooleanField(default=False)),
                ("maps_url", models.URLField()),
                ("video360_url", models.URLField()),
                ("videoblog_url", models.URLField()),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="category.category",
                    ),
                ),
            ],
        ),
    ]
