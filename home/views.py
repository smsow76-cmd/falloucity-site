# home/views.py
from django.shortcuts import render
from django.http import HttpResponse

# ✅ 27 biens avec descriptions uniques
BIENS = [
    {
        'id': 1,
        'titre': 'Immeuble Horizon',
        'short_details': 'Immeuble moderne avec vue panoramique',
        'details': 'Immeuble moderne et élégant offrant plusieurs niveaux, façades soignées, espaces lumineux et confort maximal. Idéal pour habitation ou usage professionnel.',
        'image': 'house1.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 2,
        'titre': 'Résidence Soleil',
        'short_details': 'Résidence lumineuse et contemporaine',
        'details': 'Résidence moderne offrant de grands appartements lumineux, espaces communs bien aménagés et sécurité optimale.',
        'image': 'house2.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 3,
        'titre': 'Villa Élégance',
        'short_details': 'Villa design et raffinée',
        'details': 'Villa contemporaine avec un style architectural unique, idéale pour un confort familial et des usages professionnels mixtes.',
        'image': 'house3.jpeg',
        'type_bien': 'Villa',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 4,
        'titre': 'Résidence Océan',
        'short_details': 'Bâtiment moderne proche de la mer',
        'details': 'Bâtiment élégant situé à proximité de la mer, offrant des appartements spacieux et un environnement agréable.',
        'image': 'house4.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 5,
        'titre': 'Immeuble Panorama',
        'short_details': 'Immeuble offrant de larges balcons',
        'details': 'Conçu pour le confort, avec des balcons spacieux et une vue dégagée sur Ngor/Almadies.',
        'image': 'house5.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 6,
        'titre': 'Villa Lumière',
        'short_details': 'Villa moderne avec espaces lumineux',
        'details': 'Villa contemporaine avec un aménagement intérieur optimisé pour la lumière naturelle.',
        'image': 'house6.jpeg',
        'type_bien': 'Villa',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 7,
        'titre': 'Résidence Panorama',
        'short_details': 'Résidence haut standing au cœur de Ngor',
        'details': 'Résidence moderne offrant confort et sécurité avec un design élégant et des espaces communs agréables.',
        'image': 'house7.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 8,
        'titre': 'Immeuble Prestige',
        'short_details': 'Immeuble contemporain et raffiné',
        'details': 'Bâtiment moderne et bien situé, idéal pour habitation ou usage professionnel.',
        'image': 'house8.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 9,
        'titre': 'Résidence Jardin',
        'short_details': 'Bâtiment avec jardin intégré',
        'details': 'Résidence avec espaces verts intégrés, idéale pour un cadre de vie agréable.',
        'image': 'house9.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 10,
        'titre': 'Villa Horizon',
        'short_details': 'Villa avec terrasse panoramique',
        'details': 'Villa moderne dotée d’une terrasse avec vue sur la ville et de grands espaces intérieurs.',
        'image': 'house10.jpeg',
        'type_bien': 'Villa',
        'lieu': 'Ngor/Almadies'
    },
    # 🔹 Bien 11 → 27
    {
        'id': 11,
        'titre': 'Résidence Confort',
        'short_details': 'Résidence moderne et sécurisée',
        'details': 'Résidence élégante avec un environnement calme et sécurisé.',
        'image': 'house11.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 12,
        'titre': 'Immeuble Moderne',
        'short_details': 'Bâtiment contemporain au cœur de la ville',
        'details': 'Immeuble moderne idéal pour des bureaux ou appartements spacieux.',
        'image': 'house12.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 13,
        'titre': 'Villa Jardin',
        'short_details': 'Villa avec espace vert privé',
        'details': 'Villa élégante avec jardin pour détente et loisirs, adaptée à un usage résidentiel.',
        'image': 'house13.jpeg',
        'type_bien': 'Villa',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 14,
        'titre': 'Résidence Vue',
        'short_details': 'Résidence avec vue dégagée',
        'details': 'Résidence moderne offrant une vue panoramique et des appartements spacieux.',
        'image': 'house14.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 15,
        'titre': 'Immeuble Élégance',
        'short_details': 'Bâtiment raffiné et bien situé',
        'details': 'Immeuble élégant pour habitation ou bureaux avec espaces lumineux et confortables.',
        'image': 'house15.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 16,
        'titre': 'Villa Panorama',
        'short_details': 'Villa avec grandes baies vitrées',
        'details': 'Villa contemporaine offrant luminosité et confort optimal.',
        'image': 'house16.jpeg',
        'type_bien': 'Villa',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 17,
        'titre': 'Résidence Élégante',
        'short_details': 'Résidence moderne et charmante',
        'details': 'Résidence avec design soigné et espaces optimisés pour confort et bien-être.',
        'image': 'house17.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 18,
        'titre': 'Immeuble Lumière',
        'short_details': 'Bâtiment lumineux et contemporain',
        'details': 'Immeuble moderne avec grandes ouvertures pour luminosité maximale.',
        'image': 'house18.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 19,
        'titre': 'Villa Prestige',
        'short_details': 'Villa moderne et spacieuse',
        'details': 'Villa élégante avec espaces optimisés pour confort résidentiel.',
        'image': 'house19.jpeg',
        'type_bien': 'Villa',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 20,
        'titre': 'Résidence Ciel',
        'short_details': 'Résidence avec vue sur la ville',
        'details': 'Résidence moderne avec design contemporain et espaces lumineux.',
        'image': 'house20.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 21,
        'titre': 'Immeuble Jardin',
        'short_details': 'Bâtiment avec jardin intégré',
        'details': 'Immeuble moderne avec jardin pour un cadre de vie agréable.',
        'image': 'house21.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 22,
        'titre': 'Villa Lumière',
        'short_details': 'Villa lumineuse et accueillante',
        'details': 'Villa avec aménagement moderne et confort optimal.',
        'image': 'house22.jpeg',
        'type_bien': 'Villa',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 23,
        'titre': 'Résidence Panorama',
        'short_details': 'Résidence avec balcons spacieux',
        'details': 'Résidence moderne offrant des espaces communs agréables et sécurisés.',
        'image': 'house23.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 24,
        'titre': 'Immeuble Horizon',
        'short_details': 'Bâtiment contemporain et élégant',
        'details': 'Immeuble moderne avec grandes baies vitrées et espaces lumineux.',
        'image': 'house24.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 25,
        'titre': 'Villa Confort',
        'short_details': 'Villa confortable et moderne',
        'details': 'Villa élégante offrant un cadre agréable et lumineux.',
        'image': 'house25.jpeg',
        'type_bien': 'Villa',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 26,
        'titre': 'Résidence Élégance',
        'short_details': 'Résidence moderne avec design soigné',
        'details': 'Résidence contemporaine avec confort et sécurité.',
        'image': 'house26.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
    {
        'id': 27,
        'titre': 'Immeuble Prestige',
        'short_details': 'Bâtiment moderne au cœur de Ngor',
        'details': 'Immeuble élégant offrant des appartements lumineux et spacieux.',
        'image': 'house27.jpeg',
        'type_bien': 'Immeuble',
        'lieu': 'Ngor/Almadies'
    },
]

IMAGES = [f'house{i}.jpeg' for i in range(1, 28)]

# ===== Pages =====
def index(request):
    return render(request, 'index.html', {
        'biens': BIENS[:6],
        'images': IMAGES
    })

def proprietes(request):
    biens = BIENS.copy()
    q = request.GET.get('q')
    type_bien = request.GET.get('type')

    if q:
        biens = [b for b in biens if q.lower() in b['titre'].lower() or q.lower() in b['lieu'].lower()]

    if type_bien:
        biens = [b for b in biens if b['type_bien'] == type_bien]

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