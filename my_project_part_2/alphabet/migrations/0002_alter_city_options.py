# Generated by Django 4.1.2 on 2022-10-27 12:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("alphabet", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="city",
            options={"ordering": ["name"]},
        ),
    ]