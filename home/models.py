from django.db import models

class Bien(models.Model):
    titre = models.CharField(max_length=200)
    prix = models.CharField(max_length=50, blank=True)  # optionnel si tu veux le prix
    details = models.TextField()
    image = models.ImageField(upload_to='biens/')  # si tu veux gérer des fichiers image
    type_bien = models.CharField(max_length=50, blank=True)
    lieu = models.CharField(max_length=100, default="Ngor/Almadies")

    def __str__(self):
        return self.titre