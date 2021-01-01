from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='search-players-home'),
    path('results/', views.return_search_results, name='search-results'),
]