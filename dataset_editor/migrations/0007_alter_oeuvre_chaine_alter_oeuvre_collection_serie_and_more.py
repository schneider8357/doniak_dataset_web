# Generated by Django 4.2.6 on 2024-01-23 17:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dataset_editor", "0006_alter_personne_role"),
    ]

    operations = [
        migrations.AlterField(
            model_name="oeuvre",
            name="chaine",
            field=models.CharField(verbose_name=1024),
        ),
        migrations.AlterField(
            model_name="oeuvre",
            name="collection_serie",
            field=models.CharField(verbose_name=1024),
        ),
        migrations.AlterField(
            model_name="oeuvre",
            name="duree",
            field=models.CharField(blank=True, default="", verbose_name=1024),
        ),
        migrations.AlterField(
            model_name="oeuvre",
            name="episodes_nbr",
            field=models.CharField(blank=True, default="", verbose_name=1024),
        ),
        migrations.AlterField(
            model_name="oeuvre",
            name="genre_oeuvre",
            field=models.CharField(blank=True, default="", verbose_name=1024),
        ),
        migrations.AlterField(
            model_name="oeuvre",
            name="note",
            field=models.CharField(blank=True, default="", verbose_name=1024),
        ),
        migrations.AlterField(
            model_name="oeuvre",
            name="num_saisons",
            field=models.CharField(blank=True, default="", verbose_name=1024),
        ),
        migrations.AlterField(
            model_name="oeuvre",
            name="oeuvre_titre",
            field=models.CharField(verbose_name=1024),
        ),
        migrations.AlterField(
            model_name="oeuvre",
            name="oeuvre_titre_doniak",
            field=models.CharField(verbose_name=1024),
        ),
        migrations.AlterField(
            model_name="oeuvre",
            name="source_type",
            field=models.CharField(blank=True, default="", verbose_name=1024),
        ),
        migrations.AlterField(
            model_name="oeuvre",
            name="sujet",
            field=models.CharField(blank=True, default="", verbose_name=1024),
        ),
    ]
