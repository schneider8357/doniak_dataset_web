from django import forms

from .models import Oeuvre


class DateInput(forms.DateInput):
    input_type = "date"


class OeuvreFilterForm(forms.ModelForm):
    ORDER_BY_CHOICES = [
        ("oeuvre_num_livres", "Num Oeuvre"),
        ("oeuvre_type", "Type Oeuvre"),
        ("oeuvre_titre", "Titre Oeuvre"),
        ("oeuvre_titre_doniak", "Titre Oeuvre Doniak (Original)"),
        ("collection_serie", "Collection Serie (Soustitre)"),
        ("date_diff", "Date Diffusion"),
        ("chaine", "Chaine"),
        ("episodes_nbr", "Episodes Nbr"),
        ("genre_oeuvre", "Genre"),
    ]

    order_by = forms.ChoiceField(
        label="Order By",
        choices=ORDER_BY_CHOICES,
        required=False,
    )

    desc = forms.BooleanField()

    ITEMS_PER_PAGE_CHOICES = [
        ("25", 25),
        ("50", 50),
        ("75", 75),
        ("100", 100),
        ("200", 200),
    ]

    items_per_page = forms.ChoiceField(
        label="Items per page",
        choices=ITEMS_PER_PAGE_CHOICES,
        required=False,
    )

    class Meta:
        model = Oeuvre
        fields_contains = [
            "oeuvre_titre",
            "oeuvre_titre_doniak",
            "collection_serie",
            "chaine",
            "genre_oeuvre",
        ]
        fields_equal = [
            "oeuvre_num_livres",
            "oeuvre_type",
            "date_diff",
        ]
        fields = fields_equal + fields_contains

        widgets = {
            "date_diff": DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for _, field in self.fields.items():
            field.required = False

