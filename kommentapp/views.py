from django.shortcuts import render
from .models import KommentModel
from .forms import KommentForm

def komments_view(request):
    komments = KommentModel.objects.all()
    if request.method == "POST":
        form = KommentForm(request.POST)
        if form.is_valid():
            form.save()
            form = KommentForm()
    else:
        form = KommentForm()
    return render(request, 'kommentapp/komments.html', {'komments':komments, 'komment_form':form})
    
