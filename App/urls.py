from django.urls import path 
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('', views.style, name='bootstrap'),
    path('movies', views.movie, name='movies'),
    path('series', views.serie, name='series'),
    path('movie_play/<int:movie_id>/', views.movie_play, name='movie_play'),
    path('serie_play/<int:serie_id>/', views.serie_play, name='serie_play'),
    path('search/', views.search, name='search'),
    
    
   
   
]