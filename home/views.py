from django.shortcuts import render
from django.http import HttpResponse

from falloucity.settings import EMAIL_HOST_USER

# ===== BIENS =====
BIENS = [
    {'id': 1, 'titre': 'Siège Fallou City', 'details': 'Projet de R+5 de 200 m2 avec 1 appartement par niveau, très spacieux, avec un excellent rendement locatif.- Quartier résidentiel, calme Emplacement stratégique - Opportunité unique pour les investisseurs', 'image': 'house1.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 2, 'titre': 'Immeuble Horizon', 'details': 'Projet d’immeuble moderne R+9 avec façade architecturale contemporaine, balcons spacieux et design haut de gamme. Idéal pour logements de standing ou usage mixte (commerce + habitation). Emplacement urbain stratégique, fort potentiel locatif', 'image': 'house2.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 3, 'titre': 'Immeuble Mame Dabakh', 'details': 'Immeuble résidentiel R+8 en cours de finition, avec balcons vitrés et structure moderne. Parfait pour investissement locatif avec plusieurs appartements par niveau. Situé dans une zone en développement avec bonne accessibilité', 'image': 'house3.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 4, 'titre': 'Siège Fallou City', 'details': 'Projet d’immeuble R+5 au design élégant et épuré, avec grandes terrasses et façade décorative. Adapté pour appartements familiaux confortables. Quartier calme, idéal pour résidence principale ou investissement rentable', 'image': 'house4.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 5, 'titre': 'Résidence Atlantique', 'details': 'Projet d’immeuble moderne R+9 avec plusieurs appartements par étage, offrant des espaces lumineux avec balcons. Design sobre et contemporain, idéal pour un investissement locatif rentable. Situé en zone urbaine dynamique avec accès facile aux commodités', 'image': 'house5.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 6, 'titre': 'Immeuble Mamadou Diallo', 'details': 'Immeuble résidentiel haut standing R+10 avec façade architecturale élégante et finitions modernes. Appartements bien agencés avec terrasses, parfait pour un rendement locatif élevé. Emplacement stratégique en milieu urbain attractif', 'image': 'house6.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 7, 'titre': 'Fa Bintou Mbaye', 'details': 'Projet d’immeuble R+5 au design contemporain avec 1 à 2 appartements par niveau, spacieux et bien ventilés. Architecture esthétique avec balcons et parking intégré. Idéal pour habitation ou investissement dans un quartier calme et accessible', 'image': 'house7.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 8, 'titre': 'Immeuble Océan', 'details': 'Projet d’immeuble R+5 au design contemporain avec façade géométrique moderne et balcons spacieux. Appartements lumineux et bien ventilés, avec parking en rez-de-chaussée, idéal pour habitation ou investissement', 'image': 'house8.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 9, 'titre': 'Résidence Luxe', 'details': 'Immeuble moderne R+9 au design dynamique avec façades géométriques et balcons variés. Appartements lumineux, parking en rez-de-chaussée et architecture urbaine idéale pour investissement locatif', 'image': 'house9.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 10, 'titre': 'Résidence Principale', 'details': 'Projet d’immeuble R+9 au style moderne et élégant avec façade travaillée et éléments décoratifs verticaux. Appartements confortables avec balcons, bonne luminosité et accessibilité, parfait pour un projet résidentiel ou locatif', 'image': 'house10.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 11, 'titre': 'Résidence Skyline', 'details': 'Immeuble résidentiel R+5 au design contemporain avec façade structurée et éléments décoratifs modernes. Appartements lumineux avec balcons spacieux et rez-de-chaussée commercial, idéal pour usage mixte', 'image': 'house11.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 12, 'titre': 'Immeuble Serenity', 'details': 'Immeuble résidentiel R+11 au design contemporain avec façade structurée et éléments décoratifs modernes. Appartements lumineux avec balcons spacieux et rez-de-chaussée commercial, idéal pour usage mixte', 'image': 'house12.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 13, 'titre': 'Résidence Émeraude', 'details': 'Résidence contemporaine R+9 avec lignes épurées, grandes terrasses vitrées et finitions haut de gamme. Espaces de vie spacieux, bonne luminosité et cadre élégant en milieu urbain', 'image': 'house13.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 14, 'titre': 'Immeuble Royal', 'details': 'Résidence contemporaine R+8 avec lignes épurées, grandes terrasses vitrées et finitions haut de gamme. Espaces de vie spacieux, bonne luminosité et cadre élégant en milieu urbain', 'image': 'house14.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 15, 'titre': 'Résidence Modern', 'details': 'fait la descritption bref de chaque images exemple Projet d’immeuble au design contemporain avec 1 à 2 appartements par niveau, spacieux et bien ventilés. Architecture esthétique avec balcons et parking intégré. Idéal pour habitation ou investissement dans un quartier calme et accessible', 'image': 'house15.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 16, 'titre': 'Immeuble Horizon Bleu', 'details': 'Résidence contemporaine R+10 avec lignes épurées, grandes terrasses vitrées et finitions haut de gamme. Espaces de vie spacieux, bonne luminosité et cadre élégant en milieu urbain', 'image': 'house16.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 17, 'titre': 'Résidence Paradise', 'details': 'Résidence haut standing R+9 avec architecture élégante, éclairage LED décoratif et façade travaillée. Appartements spacieux avec balcons, parfait pour un cadre de vie confortable en zone urbaine', 'image': 'house17.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 18, 'titre': 'Immeuble Gold', 'details': 'Projet à concept artistique contemporain avec aménagement extérieur en cours, incluant un sentier en béton en finition. Design moderne et original, idéal pour valoriser un espace résidentiel ou commercial avec une identité unique', 'image': 'house18.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 19, 'titre': 'Immeuble Sunset', 'details': 'Immeuble moderne au design dynamique avec façades géométriques et balcons variés. Appartements lumineux, parking en rez-de-chaussée et architecture urbaine idéale pour investissement locatif', 'image': 'house19.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 20, 'titre': 'Immeuble Sunset', 'details': 'Immeuble moderne au design dynamique avec façades géométriques et balcons variés. Appartements lumineux, parking en rez-de-chaussée et architecture urbaine idéale pour investissement locatif', 'image': 'house20.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 21, 'titre': 'Résidence Premium', 'details': 'Immeuble R+9 au style moderne avec jeux de volumes et finitions boisées. Appartements confortables avec balcons vitrés et parking intégré, parfait pour un cadre de vie urbain agréable', 'image': 'house21.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 22, 'titre': 'Immeuble Diamond', 'details': 'Immeuble au style moderne avec jeux de volumes et finitions boisées. Appartements confortables avec balcons vitrés et parking intégré, parfait pour un cadre de vie urbain agréable', 'image': 'house22.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 23, 'titre': 'Immeuble Altruiste A', 'details': 'Projet composé de trois immeubles en avec sous-sol, implantés sur une surface de 500 m². Le rez-de-chaussée est dédié à des espaces fonctionnels, comprenant des commerces, une salle de sport ainsi qu’un appartement de type F3.Les étages supérieurs sont destinés à l’habitation, avec une configuration type de deux appartements F4 et un appartement F3 par niveau.L’ensemble du projet est valorisé par un éclairage intégré, offrant un rendu moderne, haut de gamme et particulièrement attractif', 'image': 'house23.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 24, 'titre': 'Immeuble Green Park', 'details': 'Immeuble R+10 en cours de construction avec structure en béton et balcons intégrés. Projet prometteur destiné à des logements modernes, avec potentiel intéressant pour habitation ou investissement', 'image': 'house24.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 25, 'titre': 'Résidence Vista', 'details': 'Immeuble au style moderne avec jeux de volumes et finitions boisées. Appartements confortables avec balcons vitrés et parking intégré, parfait pour un cadre de vie urbain agréable', 'image': 'house25.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 26, 'titre': 'Immeuble Majestic', 'details': 'Immeuble résidentiel haut standing R+10 avec façade architecturale élégante et finitions modernes. Appartements bien agencés avec terrasses, parfait pour un rendement locatif élevé. Emplacement stratégique en milieu urbain attractif', 'image': 'house26.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 27, 'titre': 'Résidence Central', 'details': 'Projet d’immeuble au design contemporain avec façade artistique en noir et blanc. Bâtiment de grande hauteur offrant plusieurs niveaux d’appartements spacieux et lumineux, idéal pour un projet résidentiel ou mixte à forte valeur architecturale', 'image': 'house27.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
]

# ===== IMAGES CAROUSEL =====
IMAGES = [f'house{i}.jpeg' for i in range(1, 28)]

# ===== VUES =====
def index(request):
    return render(request, 'index.html', {'biens': BIENS[:6], 'images': IMAGES[:5]})

def proprietes(request):
    biens = BIENS.copy()
    q = request.GET.get('q', '').strip()
    type_bien = request.GET.get('type', '').strip()
    if q:
        biens = [b for b in biens if q.lower() in b['titre'].lower() or q.lower() in b['lieu'].lower()]
    if type_bien:
        biens = [b for b in biens if b['type_bien'].lower() == type_bien.lower()]
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

def about(request):
    return render(request, 'about.html')



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message_text
        )
        messages.success(request, "Votre message a été envoyé avec succès ! ✅")
        return redirect('contact')  # recharge la page

    return render(request, 'contact.html')

def video_presentation(request):
    return render(request, 'video.html')