# Generated by Django 4.1.6 on 2023-02-02 19:24

import autoslug.fields
import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
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
                ("title", models.CharField(max_length=250)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=False,
                        max_length=250,
                        populate_from="title",
                        unique=True,
                    ),
                ),
                ("description", models.TextField(max_length=250)),
                ("body", ckeditor.fields.RichTextField()),
                ("published", models.DateTimeField(auto_now_add=True)),
                (
                    "status",
                    models.CharField(
                        choices=[("DF", "Draft"), ("PB", "Published")],
                        default="DF",
                        max_length=2,
                    ),
                ),
            ],
            options={
                "ordering": ["-published"],
            },
        ),
        migrations.AddIndex(
            model_name="article",
            index=models.Index(
                fields=["-published"], name="api_article_publish_e8dfec_idx"
            ),
        ),
    ]
