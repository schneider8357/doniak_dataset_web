# Generated by Django 4.2.6 on 2024-02-03 01:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dataset_editor", "0010_alter_oeuvre_oeuvre_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="episode",
            name="note",
            field=models.CharField(blank=True, default="", max_length=4096),
        ),
        migrations.AlterField(
            model_name="episode",
            name="sujet",
            field=models.CharField(blank=True, default="", max_length=4096),
        ),
        migrations.AlterField(
            model_name="oeuvre",
            name="note",
            field=models.CharField(blank=True, default="", max_length=4096),
        ),
        migrations.AlterField(
            model_name="oeuvre",
            name="oeuvre_type",
            field=models.CharField(
                choices=[("unitaire", "Unitaire"), ("serie", "Série")],
                default="unitaire",
                max_length=32,
            ),
        ),
        migrations.AlterField(
            model_name="oeuvre",
            name="sujet",
            field=models.CharField(blank=True, default="", max_length=4096),
        ),
    ]
