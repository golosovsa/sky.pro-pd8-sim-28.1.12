# Generated by Django 4.1.2 on 2022-10-27 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("along_neva_channels", "0002_alter_tour_ends_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="tour",
            name="author",
            field=models.CharField(default="", max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="tour",
            name="starts_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
