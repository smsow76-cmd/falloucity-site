from django.shortcuts import render
from django.http import HttpResponse

# ===== BIENS =====

BIENS = [
    {
        'id': 1,
        'titre': 'Immeuble Horizon',
        'details': 'Immeuble avec parking',
        'image': 'house1.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor-Almadies'
    },
    {
        'id': 2,
        'titre': 'Résidence Soleil',
        'details': 'Immeuble avec ascenseur',
        'image': 'house2.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor-Almadies'
    },
    {
        'id': 3,
        'titre': 'Immeuble Élégance',
        'details': 'Immeuble avec balcon',
        'image': 'house3.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor-Almadies'
    },
]

# ===== TITRES =====

titres = [
    "Immeuble Prestige",
    "Résidence Atlantique",
    "Immeuble Palmier",
    "Résidence Standing",
    "Immeuble Océan",
    "Résidence Luxe",
    "Immeuble Panorama",
    "Résidence Skyline",
    "Immeuble Serenity",
    "Résidence Émeraude",
    "Immeuble Royal",
    "Résidence Modern",
    "Immeuble Horizon Bleu",
    "Résidence Paradise",
    "Immeuble Gold",
    "Résidence Crystal",
    "Immeuble Sunset",
    "Résidence Premium",
    "Immeuble Diamond",
    "Résidence Elite",
    "Immeuble Green Park",
    "Résidence Vista",
    "Immeuble Majestic",
    "Résidence Central"
]

# ===== DESCRIPTIONS =====

details = [
    "Immeuble avec parking",
    "Immeuble avec ascenseur",
    "Immeuble avec balcon",
    "Immeuble avec terrasse",
    "Immeuble avec parking sécurisé",
    "Immeuble moderne",
    "Immeuble avec vue sur mer",
    "Immeuble avec espace parking",
    "Immeuble avec ascenseur et balcon",
    "Immeuble avec grande terrasse",
    "Immeuble avec sécurité",
    "Immeuble avec parking et ascenseur",
    "Immeuble avec balcon et terrasse",
    "Immeuble avec vue dégagée",
    "Immeuble avec espace extérieur",
    "Immeuble moderne avec parking",
    "Immeuble avec terrasse commune",
    "Immeuble avec sécurité et parking",
    "Immeuble simple",
    "Immeuble avec parking privé",
    "Immeuble avec balcon moderne",
    "Immeuble avec terrasse ouverte",
    "Immeuble avec espace détente",
    "Immeuble avec entrée sécurisée"
]

# ===== AJOUT AUTOMATIQUE JUSQU'À 27 BIENS =====

for i in range(4, 28):
    BIENS.append({
        'id': i,
        'titre': titres[i-4],
        'details': details[i-4],
        'image': f'house{i}.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor-Almadies'
    })

# ===== IMAGES CAROUSEL =====

IMAGES = [f'house{i}.jpeg' for i in range(1, 28)]

# ===== VUES =====

def index(request):
    return render(request, 'index.html', {
        'biens': BIENS[:6],
        'images': IMAGES[:5]
    })


def proprietes(request):
    biens = BIENS.copy()

    q = request.GET.get('q', '').strip()
    type_bien = request.GET.get('type', '').strip()

    if q:
        biens = [
            b for b in biens
            if q.lower() in b['titre'].lower() or q.lower() in b['lieu'].lower()
        ]

    if type_bien:
        biens = [
            b for b in biens
            if b['type_bien'].lower() == type_bien.lower()
        ]

    return render(request, 'proprietes.html', {'biens': biens})


def detail_propriete(request, id):
    bien = next((b for b in BIENS if b['id'] == id), None)

    if not bien:
        return HttpResponse("Bien non trouvé")

    return render(request, 'detail.html', {'bien': bien})


def services(request):
    return render(request, 'services.html')


def contact(request):
    return render(request, 'contact.html')