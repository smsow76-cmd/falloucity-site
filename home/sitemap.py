from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Bien

# Sitemap pour les pages statiques
class StaticViewSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Ces noms doivent correspondre aux "name=" de tes URLs
        return ['home', 'proprietes', 'services', 'contact']

    def location(self, item):
        # Ne pas concaténer le domaine ! Django utilise le bon domaine en production
        return reverse(item)


# Sitemap pour les biens/propriétés dynamiques
class BienSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        # Retourne tous les objets Bien
        return Bien.objects.all()

    def location(self, obj):
        # Génère l'URL pour chaque bien
        return reverse('detail_propriete', args=[obj.id])