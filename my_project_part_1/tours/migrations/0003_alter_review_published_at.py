# Generated by Django 4.1.2 on 2022-10-26 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tours", "0002_review_author_review_content_review_is_published_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="published_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
