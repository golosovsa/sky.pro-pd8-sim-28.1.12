# Generated by Django 4.1.2 on 2022-10-27 07:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("discounts", "0002_alter_discount_ends_at_alter_discount_starts_at"),
    ]

    operations = [
        migrations.AlterField(
            model_name="discount",
            name="tour",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="discounts.tour",
            ),
        ),
    ]
