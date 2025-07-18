# Generated by Django 5.2.3 on 2025-07-05 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("airport", "0003_flight_crews"),
    ]

    operations = [
        migrations.AddField(
            model_name="airplane",
            name="image",
            field=models.ImageField(null=True, upload_to="uploads/"),
        ),
        migrations.AlterUniqueTogether(
            name="ticket",
            unique_together={("seat", "flight")},
        ),
    ]
