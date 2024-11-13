from django.shortcuts import render
from .models import Breed, Dog

def breed_list(request):
    breeds = Breed.objects.all()
    return render(request, 'dogs/breed_list.html', {'breeds': breeds})

def dog_list(request):
    dogs = Dog.objects.all()
    return render(request, 'dogs/dog_list.html', {'dogs': dogs})
