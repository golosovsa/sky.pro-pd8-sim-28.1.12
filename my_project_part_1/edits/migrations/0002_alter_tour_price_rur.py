# Generated by Django 4.1.2 on 2022-10-27 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("edits", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="tour",
            name="price_rur",
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]