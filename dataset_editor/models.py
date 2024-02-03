import json

from django.db import models
from multiselectfield import MultiSelectField


class Personne(models.Model):
    full_name = models.CharField(max_length=2048, null=False, blank=False)
    naissance = models.DateField(null=True)

    genre = models.CharField(max_length=1, null=True)

    COMEDIEN = 'comediens'
    REALISATEUR = 'realisateurs'
    SCENARIO = 'scenario'
    SOURCE_AUTEUR = "source_auteur"
    PIECE_DE = 'piece_de'
    MUSIQUE = 'musique'
    DECOR = 'decor'
    PRODUCTEURS = 'producteurs'
    PHOTO = 'photo'
    CAMERA = "camera"
    MISE_EN_SCENE = 'mise_en_scene'
    ASS_REAL = 'ass_real'
    MONTAGE = 'montage'
    SON = 'son'
    COSTUMES = 'costumes'
    ADAPTATION = 'adaptation'
    DIALOGUES = 'dialogues'
    OPERA_BOUFFE = 'opera_bouffe'
    OPERA = 'opera'
    DIRECTION_MUSICALE = 'direction_musicale'
    CHANSONS = 'chansons'
    DIRECTION_ARTISTIQUE = 'direction_artistique'
    OPERETTE = 'operette'
    LIVRET = 'livret'
    SPECTACLE = 'spectacle'
    TEXTE = 'texte'
    SKETCH = 'sketch'
    SAYNETE = 'saynete'
    CHOR = 'chor'
    PIECE_MTSC = 'piece_mtsc'
    OPERA_MTSC = 'opera_mtsc'
    MTSC = 'mtsc'
    ILLUST = "illust"
    ILLUST_MUSIC = "illust_music"
    GRAPHISME = "graphisme"
    DIR_PROD = "dir_prod"
    ASSISTANT = "assistant"
    CASCADES = "cascades"
    VIDEO = "video"
    SCRIPTE = "scripte"
    CONS_ART = "cons_art"
    CONS_TEC = "cons_tec"
    CONS_HIST = "cons_hist"
    EFFETS_SPEC = "effets_spec"
    PROD_DELEG = "prod_deleg"
    ANIMATION = "animation"
    MISC = "misc"


    ROLE_CHOICES = [
        (REALISATEUR, 'Réalisateur'),
        (SCENARIO, 'Scénariste'),
        (SOURCE_AUTEUR, 'Source Auteur'),
        (PIECE_DE, 'Pièce de'),
        (MUSIQUE, 'Traducteur'),
        (DECOR, 'Comédien'),
        (PRODUCTEURS, 'Musicien'),
        (PHOTO, 'Producteur'),
        (CAMERA, 'Critique'),
        (MISE_EN_SCENE, 'Mise en scène'),
        (ASS_REAL, 'Ass. Réal.'),
        (MONTAGE, 'Montage'),
        (SON, 'Son'),
        (COSTUMES, 'Costumes'),
        (ADAPTATION, 'Adaptation'),
        (DIALOGUES, 'Dialogues'),
        (OPERA_BOUFFE, 'Opéra Bouffe'),
        (OPERA, 'Opéra'),
        (DIRECTION_MUSICALE, 'Direction musicale'),
        (CHANSONS, 'Chansons'),
        (DIRECTION_ARTISTIQUE, 'Direction artistique'),
        (OPERETTE, 'Opérette'),
        (LIVRET, 'Livret'),
        (SPECTACLE, 'Spectacle'),
        (TEXTE, 'Texte'),
        (SKETCH, 'Sketch'),
        (SAYNETE, 'Saynète'),
        (CHOR, 'Chor.'),
        (PIECE_MTSC, 'Pièce Metteur en scène'),
        (OPERA_MTSC, 'Opéra Metteur en scène'),
        (MTSC, 'Metteur en scène'),
        (ILLUST, "Illustrations"),
        (ILLUST_MUSIC, "Illustration sonore/musicale"),
        (GRAPHISME, "Graphisme"),
        (DIR_PROD, "Direction prod."),
        (ASSISTANT, "Assistant"),
        (CASCADES, "Cascades"),
        (VIDEO, "Video"),
        (SCRIPTE, "Scripte"),
        (CONS_ART, "Conseiller artistique"),
        (CONS_TEC, "Conseiller technique"),
        (CONS_HIST, "Conseiller historique"),
        (EFFETS_SPEC, "Effets spéciaux"),
        (PROD_DELEG, "Producteurs délégués"),
        (ANIMATION, "Animation"),
        (MISC, "Miscellaneous"),
    ]

    role = MultiSelectField(choices=ROLE_CHOICES, null=False, max_choices=5, max_length=200)
    age = models.IntegerField(null=True)
    nationalite	= models.CharField(max_length=63, null=True)


class Oeuvre(models.Model):
    oeuvre_num_livres = models.IntegerField(null=False, blank=False, primary_key=True)

    OEUVRE_TYPE_UNITAIRE = 'unitaire'
    OEUVRE_TYPE_SERIE = 'serie'

    OEUVRE_TYPE_CHOICES = [
        (OEUVRE_TYPE_UNITAIRE, 'Unitaire'),
        (OEUVRE_TYPE_SERIE, 'Série'),
    ]

    oeuvre_type = models.CharField(
        max_length=32,
        choices=OEUVRE_TYPE_CHOICES,
        default=OEUVRE_TYPE_UNITAIRE,
        null=False,
        blank=False
    )

    feuilleton = models.BooleanField()
    oeuvre_titre = models.CharField(max_length=2048, null=False, blank=False)
    oeuvre_titre_doniak = models.CharField(max_length=2048, null=False, blank=False)
    collection_serie = models.CharField(max_length=2048, null=False, blank=False)
    date_diff = models.DateField(null=False)
    chaine = models.CharField(max_length=2048, blank=False, null=False)
    note = models.CharField(max_length=4096, blank=True, default='')
    episodes_nbr = models.CharField(max_length=2048, blank=True, default='')
    duree = models.CharField(max_length=2048, blank=True, default='')
    genre_oeuvre = models.CharField(max_length=2048, blank=True, default='')
    num_saisons = models.CharField(max_length=2048, blank=True, default='')
    sujet = models.CharField(max_length=4096, blank=True, default='')
    source_type = models.CharField(max_length=2048, blank=True, default='')
    comediens = models.ManyToManyField(Personne, related_name='role_comediens')
    adaptation = models.ManyToManyField(Personne, related_name='role_adaptation')
    photo = models.ManyToManyField(Personne, related_name='role_photo')
    mtsc = models.ManyToManyField(Personne, related_name='role_mtsc')
    saynete = models.ManyToManyField(Personne, related_name='role_saynete')
    spectacle = models.ManyToManyField(Personne, related_name='role_spectacle')
    direction_musicale = models.ManyToManyField(Personne, related_name='role_direction_musicale')
    opera_bouffe = models.ManyToManyField(Personne, related_name='role_opera_bouffe')
    livret = models.ManyToManyField(Personne, related_name='role_livret')
    ass_real = models.ManyToManyField(Personne, related_name='role_ass_real')
    operette = models.ManyToManyField(Personne, related_name='role_operette')
    chor = models.ManyToManyField(Personne, related_name='role_chor')
    piece_de = models.ManyToManyField(Personne, related_name='role_piece_de')
    source_lit = models.ManyToManyField(Personne, related_name='role_source_lit')
    musique = models.ManyToManyField(Personne, related_name='role_musique')
    sketch = models.ManyToManyField(Personne, related_name='role_sketch')
    opera = models.ManyToManyField(Personne, related_name='role_opera')
    source_auteur = models.ManyToManyField(Personne, related_name='role_source_auteur')
    decor = models.ManyToManyField(Personne, related_name='role_decor')
    costumes = models.ManyToManyField(Personne, related_name='role_costumes')
    texte = models.ManyToManyField(Personne, related_name='role_texte')
    realisateurs = models.ManyToManyField(Personne, related_name='role_realisateurs')
    dialogues = models.ManyToManyField(Personne, related_name='role_dialogues')
    montage = models.ManyToManyField(Personne, related_name='role_montage')
    son = models.ManyToManyField(Personne, related_name='role_son')
    camera = models.ManyToManyField(Personne, related_name='role_camera')
    direction_artistique = models.ManyToManyField(Personne, related_name='role_direction_artistique')
    chansons = models.ManyToManyField(Personne, related_name='role_chansons')
    producteurs = models.ManyToManyField(Personne, related_name='role_producteurs')
    scenario = models.ManyToManyField(Personne, related_name='role_scenario')
    mise_en_scene = models.ManyToManyField(Personne, related_name='role_mise_en_scene')
    


    regular_fields = [
        "oeuvre_num_livres",
        "oeuvre_type",
        "feuilleton",
        "oeuvre_titre",
        "oeuvre_titre_doniak",
        "collection_serie",
        "date_diff",
        "chaine",
        "note",
        "episodes_nbr",
        "duree",
        "genre_oeuvre",
        "num_saisons",
        "sujet",
        "source_type",
    ]
    many_to_many_fields = set([
        "comediens",
        "adaptation",
        "photo",
        "mtsc",
        "saynete",
        "spectacle",
        "direction_musicale",
        "opera_bouffe",
        "livret",
        "ass_real",
        "operette",
        "chor",
        "piece_de",
        "source_lit",
        "musique",
        "sketch",
        "opera",
        "decor",
        "costumes",
        "texte",
        "realisateurs",
        "dialogues",
        "montage",
        "son",
        "camera",
        "direction_artistique",
        "chansons",
        "producteurs",
        "scenario",
        "mise_en_scene",
    ])

    def to_json(self):
        return {
            "oeuvre_num_livres": f"{self.oeuvre_num_livres:04d}",
            "oeuvre_type": self.oeuvre_type,
            "feuilleton": self.feuilleton,
            "oeuvre_titre": self.oeuvre_titre,
            "oeuvre_titre_doniak": self.oeuvre_titre_doniak,
            "collection_serie": self.collection_serie,
            "date_diff": self.date_diff.strftime("%d-%m-%Y"),
            "chaine": self.chaine,
            "note": self.note,
            "episodes": [episode.to_json() for episode in Episode.objects.filter(oeuvre=self)],
            "episodes_nbr": self.episodes_nbr,
            "duree": self.duree,
            "genre_oeuvre": self.genre_oeuvre,
            "num_saisons": self.num_saisons,
            "sujet": self.sujet,
            "source_type": self.source_type,
            "comediens": [comedien.full_name for comedien in self.comediens.all()],
            "adaptation": [adaptation.full_name for adaptation in self.adaptation.all()],
            "photo": [photo.full_name for photo in self.photo.all()],
            "mtsc": [mtsc.full_name for mtsc in self.mtsc.all()],
            "saynete": [saynete.full_name for saynete in self.saynete.all()],
            "spectacle": [spectacle.full_name for spectacle in self.spectacle.all()],
            "direction_musicale": [direction_musicale.full_name for direction_musicale in self.direction_musicale.all()],
            "opera_bouffe": [opera_bouffe.full_name for opera_bouffe in self.opera_bouffe.all()],
            "livret": [livret.full_name for livret in self.livret.all()],
            "ass_real": [ass_real.full_name for ass_real in self.ass_real.all()],
            "operette": [operette.full_name for operette in self.operette.all()],
            "chor": [chor.full_name for chor in self.chor.all()],
            "piece_de": [piece_de.full_name for piece_de in self.piece_de.all()],
            "musique": [musique.full_name for musique in self.musique.all()],
            "sketch": [sketch.full_name for sketch in self.sketch.all()],
            "opera": [opera.full_name for opera in self.opera.all()],
            "source_auteur": [source_auteur.full_name for source_auteur in self.source_auteur.all()],
            "decor": [decor.full_name for decor in self.decor.all()],
            "costumes": [costumes.full_name for costumes in self.costumes.all()],
            "texte": [texte.full_name for texte in self.texte.all()],
            "realisateurs": [realisateurs.full_name for realisateurs in self.realisateurs.all()],
            "dialogues": [dialogues.full_name for dialogues in self.dialogues.all()],
            "montage": [montage.full_name for montage in self.montage.all()],
            "son": [son.full_name for son in self.son.all()],
            "camera": [camera.full_name for camera in self.camera.all()],
            "direction_artistique": [direction_artistique.full_name for direction_artistique in self.direction_artistique.all()],
            "chansons": [chansons.full_name for chansons in self.chansons.all()],
            "producteurs": [producteurs.full_name for producteurs in self.producteurs.all()],
            "scenario": [scenario.full_name for scenario in self.scenario.all()],
            "mise_en_scene": [mise_en_scene.full_name for mise_en_scene in self.mise_en_scene.all()],
        }


class Episode(models.Model):
    oeuvre = models.ForeignKey(Oeuvre, null=False, on_delete=models.CASCADE)
    episode_num = models.CharField(max_length=12, blank=False, null=False, unique=True)
    episode_num_part = models.CharField(max_length=12, blank=False, null=False)
    note = models.CharField(max_length=4096, blank=True, default='')
    genre = models.CharField(max_length=2048, blank=True, default='')
    sujet = models.CharField(max_length=4096, blank=True, default='')
    source_type = models.CharField(max_length=2048, blank=True, default='')
    comediens = models.ManyToManyField(Personne, related_name='ep_role_comediens')
    adaptation = models.ManyToManyField(Personne, related_name='ep_role_adaptation')
    photo = models.ManyToManyField(Personne, related_name='ep_role_photo')
    mtsc = models.ManyToManyField(Personne, related_name='ep_role_mtsc')
    saynete = models.ManyToManyField(Personne, related_name='ep_role_saynete')
    spectacle = models.ManyToManyField(Personne, related_name='ep_role_spectacle')
    direction_musicale = models.ManyToManyField(Personne, related_name='ep_role_direction_musicale')
    opera_bouffe = models.ManyToManyField(Personne, related_name='ep_role_opera_bouffe')
    livret = models.ManyToManyField(Personne, related_name='ep_role_livret')
    ass_real = models.ManyToManyField(Personne, related_name='ep_role_ass_real')
    operette = models.ManyToManyField(Personne, related_name='ep_role_operette')
    chor = models.ManyToManyField(Personne, related_name='ep_role_chor')
    piece_de = models.ManyToManyField(Personne, related_name='ep_role_piece_de')
    source_lit = models.ManyToManyField(Personne, related_name='ep_role_source_lit')
    musique = models.ManyToManyField(Personne, related_name='ep_role_musique')
    sketch = models.ManyToManyField(Personne, related_name='ep_role_sketch')
    opera = models.ManyToManyField(Personne, related_name='ep_role_opera')
    source_auteur = models.ManyToManyField(Personne, related_name='ep_role_source_auteur')
    decor = models.ManyToManyField(Personne, related_name='ep_role_decor')
    costumes = models.ManyToManyField(Personne, related_name='ep_role_costumes')
    texte = models.ManyToManyField(Personne, related_name='ep_role_texte')
    realisateurs = models.ManyToManyField(Personne, related_name='ep_role_realisateurs')
    dialogues = models.ManyToManyField(Personne, related_name='ep_role_dialogues')
    montage = models.ManyToManyField(Personne, related_name='ep_role_montage')
    son = models.ManyToManyField(Personne, related_name='ep_role_son')
    camera = models.ManyToManyField(Personne, related_name='ep_role_camera')
    direction_artistique = models.ManyToManyField(Personne, related_name='ep_role_direction_artistique')
    chansons = models.ManyToManyField(Personne, related_name='ep_role_chansons')
    producteurs = models.ManyToManyField(Personne, related_name='ep_role_producteurs')
    scenario = models.ManyToManyField(Personne, related_name='ep_role_scenario')
    mise_en_scene = models.ManyToManyField(Personne, related_name='ep_role_mise_en_scene')

    regular_fields = set([
        "episode_num",
        "note",
        "genre",
        "sujet",
        "source_type",
    ])
    many_to_many_fields = set([
        "comediens",
        "adaptation",
        "photo",
        "mtsc",
        "saynete",
        "spectacle",
        "direction_musicale",
        "opera_bouffe",
        "livret",
        "ass_real",
        "operette",
        "chor",
        "piece_de",
        "source_lit",
        "musique",
        "sketch",
        "opera",
        "decor",
        "costumes",
        "texte",
        "realisateurs",
        "dialogues",
        "montage",
        "son",
        "camera",
        "direction_artistique",
        "chansons",
        "producteurs",
        "scenario",
        "mise_en_scene",
    ])

    def to_json(self):
        return {
            "oeuvre": self.oeuvre.oeuvre_num_livres,
            "episode_num": self.episode_num,
            "episode_num_part": self.episode_num_part,
            "note": self.note,
            "genre": self.genre,
            "sujet": self.sujet,
            "source_type": self.source_type,
            "comediens": [comedien.full_name for comedien in self.comediens.all()],
            "adaptation": [adaptation.full_name for adaptation in self.adaptation.all()],
            "photo": [photo.full_name for photo in self.photo.all()],
            "mtsc": [mtsc.full_name for mtsc in self.mtsc.all()],
            "saynete": [saynete.full_name for saynete in self.saynete.all()],
            "spectacle": [spectacle.full_name for spectacle in self.spectacle.all()],
            "direction_musicale": [direction_musicale.full_name for direction_musicale in self.direction_musicale.all()],
            "opera_bouffe": [opera_bouffe.full_name for opera_bouffe in self.opera_bouffe.all()],
            "livret": [livret.full_name for livret in self.livret.all()],
            "ass_real": [ass_real.full_name for ass_real in self.ass_real.all()],
            "operette": [operette.full_name for operette in self.operette.all()],
            "chor": [chor.full_name for chor in self.chor.all()],
            "piece_de": [piece_de.full_name for piece_de in self.piece_de.all()],
            "musique": [musique.full_name for musique in self.musique.all()],
            "sketch": [sketch.full_name for sketch in self.sketch.all()],
            "opera": [opera.full_name for opera in self.opera.all()],
            "source_auteur": [source_auteur.full_name for source_auteur in self.source_auteur.all()],
            "decor": [decor.full_name for decor in self.decor.all()],
            "costumes": [costumes.full_name for costumes in self.costumes.all()],
            "texte": [texte.full_name for texte in self.texte.all()],
            "realisateurs": [realisateurs.full_name for realisateurs in self.realisateurs.all()],
            "dialogues": [dialogues.full_name for dialogues in self.dialogues.all()],
            "montage": [montage.full_name for montage in self.montage.all()],
            "son": [son.full_name for son in self.son.all()],
            "camera": [camera.full_name for camera in self.camera.all()],
            "direction_artistique": [direction_artistique.full_name for direction_artistique in self.direction_artistique.all()],
            "chansons": [chansons.full_name for chansons in self.chansons.all()],
            "producteurs": [producteurs.full_name for producteurs in self.producteurs.all()],
            "scenario": [scenario.full_name for scenario in self.scenario.all()],
            "mise_en_scene": [mise_en_scene.full_name for mise_en_scene in self.mise_en_scene.all()],
        }
