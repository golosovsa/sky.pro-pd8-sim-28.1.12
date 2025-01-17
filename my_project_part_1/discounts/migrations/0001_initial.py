# Generated by Django 4.1.2 on 2022-10-27 06:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tour",
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
                ("name", models.CharField(max_length=200)),
                ("author", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="Discount",
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
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("promo", "Промокод"),
                            ("campaign", "Акция"),
                            ("discount", "Скидка"),
                        ],
                        default="promo",
                        max_length=8,
                    ),
                ),
                ("discount", models.SmallIntegerField()),
                ("code", models.CharField(max_length=50)),
                ("starts_at", models.DateField(null=True)),
                ("ends_at", models.DateField(null=True)),
                (
                    "tour",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="discounts.tour"
                    ),
                ),
            ],
        ),
    ]
