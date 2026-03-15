from django.shortcuts import render
from .forms import *
from .models import Parcel

# Create your views here.
def home_page(request):

    return render(request, 'index.html', context={'nb_colis': Parcel.objects.count()})

def parcels_page(request):
    return render(request, 'parcels.html', context={'nb_colis': Parcel.objects.all()})

def add_parcel(request):

    if request.method == 'POST':
        form = AddParcelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'index.html', context={'nb_colis': Parcel.objects.count()})
    else:
        form = AddParcelForm()
        return render(request, 'add_parcel.html', context={'form': form})
    
def tracking(request):
    parcel = None
    error = None
    if request.method == 'POST':
        tracking_number = request.POST.get('tracking_number')
        try:
            parcel = Parcel.objects.get(tracking_number=tracking_number)
        except Parcel.DoesNotExist:
            error = "Numéro de suivi invalide."
    
    return render(request, 'tracking.html', context={'error': error, 'parcel': parcel})