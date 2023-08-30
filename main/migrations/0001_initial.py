# Generated by Django 4.2.4 on 2023-08-30 15:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Theme",
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
                ("theme", models.CharField(max_length=50, verbose_name="Тема")),
            ],
        ),
        migrations.CreateModel(
            name="Problem",
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
                ("contest_id", models.IntegerField(verbose_name="Порядковый номер")),
                ("index", models.CharField(max_length=10, verbose_name="Индекс")),
                ("title", models.CharField(max_length=150, verbose_name="Название")),
                ("solve_count", models.PositiveIntegerField(verbose_name="Раз решено")),
                ("difficulty", models.PositiveIntegerField(verbose_name="Сложность")),
                (
                    "theme",
                    models.ManyToManyField(
                        blank=True,
                        default="NULL",
                        null=True,
                        related_name="problem",
                        to="main.theme",
                        verbose_name="Тема",
                    ),
                ),
            ],
        ),
    ]