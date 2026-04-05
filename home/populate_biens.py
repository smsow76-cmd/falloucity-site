# home/populate_biens.py
from .models import Bien

# Liste des 3 premiers biens avec détails uniques
BIENS = [
    {'id': 1, 'titre': 'Immeuble Horizon', 'details': 'Immeuble moderne avec vue panoramique', 'image': 'house1.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor/Almadies'},
    {'id': 2, 'titre': 'Résidence Soleil', 'details': 'Résidence lumineuse', 'image': 'house2.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor/Almadies'},
    {'id': 3, 'titre': 'Villa Élégance', 'details': 'Villa design moderne', 'image': 'house3.jpeg', 'type_bien': 'Villa', 'lieu': 'Ngor/Almadies'},
]

# Ajouter automatiquement les biens 4 à 27 avec détails simples et différents
for i in range(4, 28):
    description = f"Bien immobilier moderne {i}" if i % 2 == 0 else f"Villa moderne {i}"
    BIENS.append({
        'id': i,
        'titre': f'Bien {i}',
        'details': description,
        'image': f'house{i}.jpeg',
        'type_bien': 'Immeuble' if i % 2 == 0 else 'Villa',
        'lieu': 'Ngor/Almadies'
    })

def run():
    for bien_data in BIENS:
        # Vérifie si le bien existe déjà
        if not Bien.objects.filter(titre=bien_data['titre']).exists():
            Bien.objects.create(
                titre=bien_data['titre'],
                details=bien_data['details'],
                image=bien_data['image'],
                type_bien=bien_data['type_bien'],
                lieu=bien_data['lieu']
            )
    print("✅ Tous les biens ont été ajoutés sans doublon.")