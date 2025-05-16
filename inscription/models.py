from django.db import models

class Inscription(models.Model):
    CHOICES_TYPE = [
        ('licence_twin', 'LICENCE TWIN'),
        ('licence_srit', 'LICENCE SRIT'),
        ('master_informatique', 'MASTER INFORMATIQUE'),
    ]

    id = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    niveauEtude = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    etablissementOrigine = models.CharField(max_length=200)
    concoursSouhaiter = models.CharField(max_length=150, choices=CHOICES_TYPE)

    extraitNaissance = models.FileField(upload_to='documents/extrait/')
    certificatNationalite = models.FileField(upload_to='documents/certificat/')
    lettreMotivation = models.FileField(upload_to='documents/lettre/')
    diplome = models.FileField(upload_to='documents/diplome/')
    photo = models.ImageField(upload_to='documents/photo/')

    date_inscription = models.DateTimeField(auto_now_add=True)
    numero_inscription = models.CharField(max_length=100, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Vérifie si l'objet est nouveau (pas encore d'ID)
        is_new = self.pk is None
        super().save(*args, **kwargs)

        # Génère le numéro d’inscription après première sauvegarde
        if is_new and not self.numero_inscription:
            self.numero_inscription = f"ESATIC-{self.concoursSouhaiter.upper()}-{self.pk:04d}"
            super().save(update_fields=['numero_inscription'])

    def __str__(self):
        return f"{self.prenom} {self.nom} ({self.numero_inscription})"
