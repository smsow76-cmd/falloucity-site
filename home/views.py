from django.shortcuts import render
from django.http import HttpResponse

from falloucity.settings import EMAIL_HOST_USER

# ===== BIENS =====
BIENS = [
    {'id': 1, 'titre': 'Siège Fallou City', 'details': 'Immeuble avec parking', 'image': 'house1.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 2, 'titre': 'Immeuble Horizon', 'details': 'Immeuble avec ascenseur', 'image': 'house2.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 3, 'titre': 'Immeuble Mame Dabakh', 'details': 'Immeuble avec balcon', 'image': 'house3.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 4, 'titre': 'Siège Fallou City', 'details': 'Immeuble avec parking sécurisé', 'image': 'house4.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 5, 'titre': 'Résidence Atlantique', 'details': 'Immeuble moderne avec ascenseur', 'image': 'house5.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 6, 'titre': 'Immeuble Mamadou Diallo', 'details': 'Immeuble avec balcon et terrasse', 'image': 'house6.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 7, 'titre': 'Fa Bintou Mbaye', 'details': 'Immeuble avec grande terrasse', 'image': 'house7.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 8, 'titre': 'Immeuble Océan', 'details': 'Immeuble avec vue sur mer', 'image': 'house8.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 9, 'titre': 'Résidence Luxe', 'details': 'Immeuble moderne avec parking', 'image': 'house9.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 10, 'titre': 'Résidence Principale', 'details': 'Immeuble avec espace extérieur', 'image': 'house10.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 11, 'titre': 'Résidence Skyline', 'details': 'Immeuble avec terrasse commune', 'image': 'house11.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 12, 'titre': 'Immeuble Serenity', 'details': 'Immeuble avec sécurité et parking', 'image': 'house12.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 13, 'titre': 'Résidence Émeraude', 'details': 'Immeuble simple et moderne', 'image': 'house13.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 14, 'titre': 'Immeuble Royal', 'details': 'Immeuble avec balcon moderne', 'image': 'house14.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 15, 'titre': 'Résidence Modern', 'details': 'Immeuble avec terrasse ouverte', 'image': 'house15.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 16, 'titre': 'Immeuble Horizon Bleu', 'details': 'Immeuble avec espace détente', 'image': 'house16.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 17, 'titre': 'Résidence Paradise', 'details': 'Immeuble avec entrée sécurisée', 'image': 'house17.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 18, 'titre': 'Immeuble Gold', 'details': 'Immeuble moderne avec parking et balcon', 'image': 'house18.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 19, 'titre': 'Résidence Crystal', 'details': 'Immeuble avec terrasse et vue dégagée', 'image': 'house19.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 20, 'titre': 'Immeuble Sunset', 'details': 'Immeuble avec espace extérieur et parking', 'image': 'house20.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 21, 'titre': 'Résidence Premium', 'details': 'Immeuble moderne avec ascenseur', 'image': 'house21.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 22, 'titre': 'Immeuble Diamond', 'details': 'Immeuble avec balcon et terrasse', 'image': 'house22.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 23, 'titre': 'Immeuble Altruiste A', 'details': 'Immeuble avec grande terrasse et sécurité', 'image': 'house23.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 24, 'titre': 'Immeuble Green Park', 'details': 'Immeuble moderne et sécurisé', 'image': 'house24.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 25, 'titre': 'Résidence Vista', 'details': 'Immeuble avec parking privé', 'image': 'house25.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 26, 'titre': 'Immeuble Majestic', 'details': 'Immeuble avec balcon moderne', 'image': 'house26.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
    {'id': 27, 'titre': 'Résidence Central', 'details': 'Immeuble avec terrasse ouverte et espace détente', 'image': 'house27.jpeg', 'type_bien': 'Immeuble', 'lieu': 'Ngor-Almadies'},
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