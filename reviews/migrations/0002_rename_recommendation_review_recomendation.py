# Generated by Django 4.1.2 on 2022-11-07 00:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="recommendation",
            new_name="recomendation",
        ),
    ]
