from django.shortcuts import render
from django.http import HttpResponse

# ✅ DONNÉES (OBLIGATOIRE)
BIENS = [
    {
        'id': 1,
        'titre': 'Immeuble Horizon',
        'details': 'Immeuble moderne avec vue panoramique',
        'image': 'house1.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 2,
        'titre': 'Résidence Soleil',
        'details': 'Résidence lumineuse',
        'image': 'house2.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 3,
        'titre': 'Villa Élégance',
        'details': 'Villa design moderne',
        'image': 'house3.jpeg',
        'type_bien': 'Villa',
        'lieu': 'Ngor/Almadies'
    },
]

# 👉 Génération automatique jusqu’à 27 biens
for i in range(4, 28):
    BIENS.append({
        'id': i,
        'titre': f'Bien {i}',
        'details': 'Bien immobilier moderne',
        'image': f'house{i}.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    })

# ✅ Images
IMAGES = [f'house{i}.jpeg' for i in range(1, 28)]

# ===== VUES =====

def index(request):
    return render(request, 'index.html', {
        'biens': BIENS[:6],
        'images': IMAGES
    })


def proprietes(request):
    biens = BIENS.copy()

    q = request.GET.get('q', '').strip()
    type_bien = request.GET.get('type', '').strip()

    if q:
        biens = [
            b for b in biens
            if q.lower() in b['titre'].lower()
            or q.lower() in b['lieu'].lower()
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