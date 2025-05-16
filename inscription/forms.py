from django import forms
from .models import Inscription

class InscriptionForm(forms.ModelForm):
    class Meta:
        model = Inscription
        fields = [
            'nom', 'prenom', 'niveauEtude', 'email', 'etablissementOrigine',
            'concoursSouhaiter', 'extraitNaissance', 'certificatNationalite',
            'lettreMotivation', 'diplome', 'photo'
        ]
        widgets = {
            'nom': forms.TextInput(attrs={
                'class': 'input input-bordered w-full'
            }),
            'prenom': forms.TextInput(attrs={
                'class': 'input input-bordered w-full'
            }),
            'niveauEtude': forms.TextInput(attrs={
                'class': 'input input-bordered w-full'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'input input-bordered w-full'
            }),
            'etablissementOrigine': forms.TextInput(attrs={
                'class': 'input input-bordered w-full'
            }),
            'concoursSouhaiter': forms.Select(attrs={
                'class': 'select select-bordered w-full'
            }),
            'extraitNaissance': forms.FileInput(attrs={
                'class': 'file-input file-input-bordered w-full'
            }),
            'certificatNationalite': forms.FileInput(attrs={
                'class': 'file-input file-input-bordered w-full'
            }),
            'lettreMotivation': forms.FileInput(attrs={
                'class': 'file-input file-input-bordered w-full'
            }),
            'diplome': forms.FileInput(attrs={
                'class': 'file-input file-input-bordered w-full'
            }),
            'photo': forms.FileInput(attrs={
                'class': 'file-input file-input-bordered w-full'
            }),
        }
