# Generated by Django 3.2.5 on 2022-05-15 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="YouTube",
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
                ("index", models.IntegerField()),
                ("channelId", models.CharField(max_length=100)),
                ("IdVideo", models.CharField(max_length=100)),
                ("profile", models.URLField()),
                ("title", models.CharField(max_length=256)),
                ("thumbnails", models.URLField()),
            ],
        ),
    ]
