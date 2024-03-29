# Generated by Django 4.2.6 on 2023-11-16 20:41

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Personne",
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
                ("full_name", models.CharField(max_length=255)),
                ("naissance", models.DateField(null=True)),
                ("genre", models.CharField(max_length=1, null=True)),
                (
                    "role",
                    multiselectfield.db.fields.MultiSelectField(
                        choices=[
                            ("realisateurs", "Réalisateur"),
                            ("scenario", "Scénariste"),
                            ("source_auteur", "Source Auteur"),
                            ("piece_de", "Pièce de"),
                            ("musique", "Traducteur"),
                            ("decor", "Comédien"),
                            ("producteurs", "Musicien"),
                            ("photo", "Producteur"),
                            ("camera", "Critique"),
                            ("mise_en_scene", "Mise en scène"),
                            ("ass_real", "Ass. Réal."),
                            ("montage", "Montage"),
                            ("son", "Son"),
                            ("costumes", "Costumes"),
                            ("adaptation", "Adaptation"),
                            ("dialogues", "Dialogues"),
                            ("opera_bouffe", "Opéra Bouffe"),
                            ("opera", "Opéra"),
                            ("direction_musicale", "Direction musicale"),
                            ("chansons", "Chansons"),
                            ("direction_artistique", "Direction artistique"),
                            ("operette", "Opérette"),
                            ("livret", "Livret"),
                            ("spectacle", "Spectacle"),
                            ("texte", "Texte"),
                            ("sketch", "Sketch"),
                            ("saynete", "Saynète"),
                            ("chor", "Chor."),
                            ("piece_mtsc", "Pièce Metteur en scène"),
                            ("opera_mtsc", "Opéra Metteur en scène"),
                            ("mtsc", "Metteur en scène"),
                        ],
                        max_length=200,
                    ),
                ),
                ("age", models.IntegerField(null=True)),
                ("nationalite", models.CharField(max_length=63, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Oeuvre",
            fields=[
                (
                    "oeuvre_num_livres",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                (
                    "oeuvre_type",
                    models.CharField(
                        choices=[("unitaire", "Unitaire"), ("série", "Série")],
                        default="unitaire",
                        max_length=255,
                    ),
                ),
                ("feuilleton", models.BooleanField()),
                ("oeuvre_titre", models.CharField(max_length=255)),
                ("oeuvre_titre_doniak", models.CharField(max_length=255)),
                ("collection_serie", models.CharField(max_length=255)),
                ("date_diff", models.DateField()),
                ("chaine", models.CharField(max_length=255)),
                ("note", models.CharField(blank=True, default="", max_length=255)),
                ("episodes", models.CharField(blank=True, default="", max_length=255)),
                (
                    "episodes_nbr",
                    models.CharField(blank=True, default="", max_length=255),
                ),
                ("duree", models.CharField(blank=True, default="", max_length=255)),
                (
                    "genre_oeuvre",
                    models.CharField(blank=True, default="", max_length=255),
                ),
                (
                    "num_saisons",
                    models.CharField(blank=True, default="", max_length=255),
                ),
                ("sujet", models.CharField(blank=True, default="", max_length=255)),
                (
                    "source_type",
                    models.CharField(blank=True, default="", max_length=255),
                ),
                (
                    "adaptation",
                    models.ManyToManyField(
                        related_name="role_adaptation", to="dataset_editor.personne"
                    ),
                ),
                (
                    "ass_real",
                    models.ManyToManyField(
                        related_name="role_ass_real", to="dataset_editor.personne"
                    ),
                ),
                (
                    "camera",
                    models.ManyToManyField(
                        related_name="role_camera", to="dataset_editor.personne"
                    ),
                ),
                (
                    "chansons",
                    models.ManyToManyField(
                        related_name="role_chansons", to="dataset_editor.personne"
                    ),
                ),
                (
                    "chor",
                    models.ManyToManyField(
                        related_name="role_chor", to="dataset_editor.personne"
                    ),
                ),
                (
                    "comediens",
                    models.ManyToManyField(
                        related_name="role_comediens", to="dataset_editor.personne"
                    ),
                ),
                (
                    "costumes",
                    models.ManyToManyField(
                        related_name="role_costumes", to="dataset_editor.personne"
                    ),
                ),
                (
                    "decor",
                    models.ManyToManyField(
                        related_name="role_decor", to="dataset_editor.personne"
                    ),
                ),
                (
                    "dialogues",
                    models.ManyToManyField(
                        related_name="role_dialogues", to="dataset_editor.personne"
                    ),
                ),
                (
                    "direction_artistique",
                    models.ManyToManyField(
                        related_name="role_direction_artistique",
                        to="dataset_editor.personne",
                    ),
                ),
                (
                    "direction_musicale",
                    models.ManyToManyField(
                        related_name="role_direction_musicale",
                        to="dataset_editor.personne",
                    ),
                ),
                (
                    "livret",
                    models.ManyToManyField(
                        related_name="role_livret", to="dataset_editor.personne"
                    ),
                ),
                (
                    "mise_en_scene",
                    models.ManyToManyField(
                        related_name="role_mise_en_scene", to="dataset_editor.personne"
                    ),
                ),
                (
                    "montage",
                    models.ManyToManyField(
                        related_name="role_montage", to="dataset_editor.personne"
                    ),
                ),
                (
                    "mtsc",
                    models.ManyToManyField(
                        related_name="role_mtsc", to="dataset_editor.personne"
                    ),
                ),
                (
                    "musique",
                    models.ManyToManyField(
                        related_name="role_musique", to="dataset_editor.personne"
                    ),
                ),
                (
                    "opera",
                    models.ManyToManyField(
                        related_name="role_opera", to="dataset_editor.personne"
                    ),
                ),
                (
                    "opera_bouffe",
                    models.ManyToManyField(
                        related_name="role_opera_bouffe", to="dataset_editor.personne"
                    ),
                ),
                (
                    "operette",
                    models.ManyToManyField(
                        related_name="role_operette", to="dataset_editor.personne"
                    ),
                ),
                (
                    "photo",
                    models.ManyToManyField(
                        related_name="role_photo", to="dataset_editor.personne"
                    ),
                ),
                (
                    "piece_de",
                    models.ManyToManyField(
                        related_name="role_piece_de", to="dataset_editor.personne"
                    ),
                ),
                (
                    "producteurs",
                    models.ManyToManyField(
                        related_name="role_producteurs", to="dataset_editor.personne"
                    ),
                ),
                (
                    "realisateurs",
                    models.ManyToManyField(
                        related_name="role_realisateurs", to="dataset_editor.personne"
                    ),
                ),
                (
                    "saynete",
                    models.ManyToManyField(
                        related_name="role_saynete", to="dataset_editor.personne"
                    ),
                ),
                (
                    "scenario",
                    models.ManyToManyField(
                        related_name="role_scenario", to="dataset_editor.personne"
                    ),
                ),
                (
                    "sketch",
                    models.ManyToManyField(
                        related_name="role_sketch", to="dataset_editor.personne"
                    ),
                ),
                (
                    "son",
                    models.ManyToManyField(
                        related_name="role_son", to="dataset_editor.personne"
                    ),
                ),
                (
                    "source_auteur",
                    models.ManyToManyField(
                        related_name="role_source_auteur", to="dataset_editor.personne"
                    ),
                ),
                (
                    "source_lit",
                    models.ManyToManyField(
                        related_name="role_source_lit", to="dataset_editor.personne"
                    ),
                ),
                (
                    "spectacle",
                    models.ManyToManyField(
                        related_name="role_spectacle", to="dataset_editor.personne"
                    ),
                ),
                (
                    "texte",
                    models.ManyToManyField(
                        related_name="role_texte", to="dataset_editor.personne"
                    ),
                ),
            ],
        ),
    ]
