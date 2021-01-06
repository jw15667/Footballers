from django.shortcuts import render, redirect
from django.http import HttpResponse
from search_players.forms import SearchPlayersForm
from urllib.parse import urlencode
from utils.utils import TeammateService



def home(request):
    if request.method == 'POST':
        returned_form = SearchPlayersForm(request.POST)
        if returned_form.is_valid():
            query_string =  urlencode({'p_one': request.POST['player1'], 'p_two': request.POST['player2']})
            base_url = 'results/'
            url = '{}?{}'.format(base_url, query_string)
        return redirect(url)
    form = SearchPlayersForm()
    ctx = {
        'header': 'Search Players',
        'form': form
    }
    return render(request, 'search_players/home.html', ctx)

def return_search_results(request):
    teammate_service = TeammateService(
        request.GET['p_one'],
        request.GET['p_two']
    )
    teammates = teammate_service.calculate_mutual_teammates()
    ctx = {
        'teammates': teammates,
        'header': 'Search Players Results'
    }
    return render(request, 'search_players/results.html', ctx)

