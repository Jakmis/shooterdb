from django import forms
from .models import Result, Person, Club, Competition, Gun, Trainer

class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ['shooter', 'competition', 'discipline', 'score', 'rank', 'series']
        labels = {
            'shooter': 'Střelec',
            'competition': 'Závod',
            'discipline': 'Disciplína',
            'score': 'Skóre',
            'rank': 'Pořadí',
            'series': 'Série',
        }
        widgets = {
            'shooter': forms.Select(attrs={'class': 'form-control'}),
            'competition': forms.Select(attrs={'class': 'form-control'}),
            'discipline': forms.Select(attrs={'class': 'form-control'}),
            'score': forms.NumberInput(attrs={'class': 'form-control'}),
            'rank': forms.NumberInput(attrs={'class': 'form-control'}),
            'series': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['person_id', 'fname', 'sname', 'date_of_birth', 'club']
        labels = {
            'person_id': 'Evidenční číslo',
            'fname': 'Jméno',
            'sname': 'Příjmení',
            'date_of_birth': 'Datum narození',
            'club': 'Klub',
        }
        widgets = {
            'person_id': forms.TextInput(attrs={'class': 'form-control'}),
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'sname': forms.TextInput(attrs={'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
            'club': forms.Select(attrs={'class': 'form-control'}),
        }

class ClubForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = ['club_id', 'name']
        labels = {
            'club_id': 'Evidenční číslo klubu',
            'name': 'Název klubu',
        }
        widgets = {
            'club_id': forms.TextInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CompetitionForm(forms.ModelForm):
    class Meta:
        model = Competition
        fields = ['name', 'date', 'location', 'disciplines', 'categories', 'organizer', 'referees']
        labels = {
            'name': 'Název závodu',
            'date': 'Datum závodu',
            'location': 'Místo konání',
            'disciplines': 'Disciplíny',
            'categories': 'Kategorie',
            'organizer': 'Pořadatel',
            'referees': 'Rozhodčí',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'disciplines': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'categories': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'organizer': forms.Select(attrs={'class': 'form-control'}),
            'referees': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

class GunForm(forms.ModelForm):
    class Meta:
        model = Gun
        fields = ['gun_type', 'brand', 'model', 'caliber', 'owner']
        labels = {
            'gun_type': 'Typ zbraně',
            'brand': 'Značka',
            'model': 'Model',
            'caliber': 'Kalibr',
            'owner': 'Majitel',
        }
        widgets = {
            'gun_type': forms.Select(attrs={'class': 'form-control'}),
            'brand': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'caliber': forms.TextInput(attrs={'class': 'form-control'}),
            'owner': forms.Select(attrs={'class': 'form-control'}),
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['person', 'license_number', 'specialization']
        widgets = {
            'person': forms.Select(attrs={'class': 'form-control'}),
            'license_number': forms.TextInput(attrs={'class': 'form-control'}),
            'specialization': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }