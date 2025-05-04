from django import forms
from .models import Result

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        competition = cleaned_data.get("competition")
        category = cleaned_data.get("category")

        if competition and category and category not in competition.categories.all():
            self.add_error('category', f"Kategorie '{category}' není součástí závodu '{competition}'.")