# home/sitemap.py
from django.contrib.sitemaps import Sitemap
from .models import Bien

class BienSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Bien.objects.all()

    def location(self, obj):
        return f"/detail/{obj.id}/"