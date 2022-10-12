# Generated by Django 4.1.1 on 2022-10-12 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shortener", "0002_link_session"),
    ]

    operations = [
        migrations.CreateModel(
            name="LinkTemplate",
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
                    "name",
                    models.CharField(max_length=255, verbose_name="Название шаблона"),
                ),
                ("url", models.URLField(verbose_name="Ссылка")),
            ],
        ),
    ]
