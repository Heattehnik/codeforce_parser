# Generated by Django 4.2.4 on 2023-08-30 16:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="problem",
            name="theme",
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name="problem",
                to="main.theme",
                verbose_name="Тема",
            ),
        ),
    ]
