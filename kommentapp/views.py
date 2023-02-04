from django.shortcuts import render
from .models import KommentModel

def komments_view(request):
    komments = KommentModel.objects.all()
    return render(request, 'kommentapp/komments.html', {'komments':komments})