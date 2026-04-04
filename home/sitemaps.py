# home/sitemaps.py
from django.contrib.sitemaps import Sitemap
from .views import BIENS  # on utilise directement ta liste BIENS

class BienSitemap(Sitemap):
    changefreq = "weekly"  # Google saura que les pages sont mises à jour chaque semaine
    priority = 0.8          # priorité de ces pages dans le sitemap

    def items(self):
        return BIENS  # retourne tous les biens

    def location(self, obj):
        # Retourne l'URL de détail pour chaque bien
        return f"/proprietes/{obj['id']}/"