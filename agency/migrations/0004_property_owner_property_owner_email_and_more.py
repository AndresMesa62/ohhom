# Generated by Django 4.1.6 on 2023-02-09 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("agency", "0003_alter_property_maps_url_alter_property_video360_url_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="property",
            name="owner",
            field=models.CharField(default="Ohom", max_length=200),
        ),
        migrations.AddField(
            model_name="property",
            name="owner_email",
            field=models.CharField(default="ohom.adm@gmail.com", max_length=200),
        ),
        migrations.AddField(
            model_name="property",
            name="owner_id",
            field=models.CharField(default="Ohom", max_length=200),
        ),
        migrations.AlterField(
            model_name="property",
            name="address",
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
