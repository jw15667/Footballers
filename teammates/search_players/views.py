from django.shortcuts import render
from django.http import HttpResponse
from search_players.forms import SearchPlayersForm
from utils.utils import TeammateService


def home(request):
    if request.method == 'POST':
        returned_form = SearchPlayersForm(request.POST)
        if returned_form.is_valid():
            teammate_service = TeammateService(
                request.POST['player1'],
                request.POST['player2']
            )
            teammates = teammate_service.calculate_mutual_teammates()
            ctx = {
                'form': returned_form,
                'teammates': teammates,
                'header': 'Search Players Results'
            }
        return render(request, 'search_players/home.html', ctx)
    form = SearchPlayersForm()
    ctx = {
        'header': 'Search Players',
        'form': form
    }
    return render(request, 'search_players/home.html', ctx)

def return_search_results(request):
    return render(request, 'search_players/results.html', {'header': 'Results'})

