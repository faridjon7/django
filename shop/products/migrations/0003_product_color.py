# Generated by Django 4.1.7 on 2023-03-01 18:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0002_product_excerpt"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="color",
            field=models.CharField(
                choices=[("RED", "Red"), ("GREEN", "Green"), ("BLUE", "Red")],
                default="RED",
                max_length=32,
            ),
        ),
    ]
