from django.http import Http404, HttpResponse
from django.template.loader import get_template
from django.template import Context
import datetime
from django.shortcuts import render_to_response, render
from django.template.loader import render_to_string
from .models import Player


#def current_datetime(request):
#    now = datetime.datetime.now()
#    t = get_template('current_datetime.html')
#    html = t.render(Context({'current_date': now}))
#    return HttpResponse(html)

def hello(request):
    return HttpResponse("Hello world")
    
def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return HttpResponse(html)


def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html', {'current_date': now})

def home(request):
    return render(request, 'search_form.html')
    
    
def search(request):
    results = Player.objects.player_names('Wayne Bridge', 'John Terry')
    
    return render(request, 'results.html', {"my_list":results})
 
def add(request):
    val1 = request.GET['Player1']
    val2 = request.GET['Player2']
    results = Player.objects.player_names(val1, val2)
    return render(request, 'results.html', {"my_list":results, "player1": val1, "player2":val2})
    

    

 

    
