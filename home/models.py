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
    

from django.db import models

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.email}"