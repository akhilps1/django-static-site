from django.shortcuts import render
from .models import Place, Teams
# Create your views here.


def home(request):
    place_obj = Place.objects.all()
    team_obj = Teams.objects.all()
    return render(request, 'index.html', {'places': place_obj, 'teams': team_obj})
