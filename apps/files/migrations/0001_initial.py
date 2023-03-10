# Generated by Django 4.1.1 on 2022-10-17 07:53

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Session",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "input_file",
                    models.FileField(blank=True, null=True, upload_to="input"),
                ),
                (
                    "zip_file",
                    models.FileField(blank=True, null=True, upload_to="zip_files"),
                ),
                (
                    "output_file",
                    models.FileField(blank=True, null=True, upload_to="output"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
