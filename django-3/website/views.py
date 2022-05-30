from django.shortcuts import render
from .models import Home, Image

def about(request):
    home = Home.objects.all()
    images = Image.objects.all()
    context = {
        "home": home,
        "images": images
    }
    return render(request, 'base.html', context)
