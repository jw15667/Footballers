from django.shortcuts import render
from .models import First_player

def home(request):
    all_members = First_player.objects.all
    return render(request, 'home.html', {'all':all_members})