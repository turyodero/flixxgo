from django.shortcuts import render ,get_object_or_404
from .models import Movie , Serie
from django.db.models import Q
from itertools import chain
from django.core.paginator import Paginator


# Create your views here.
def style(request):
    return render(request,'bootstrap.html')


def about(request):
    return render(request,'about.html')

def index(request):
     movies = Movie.objects.all()
     return render(request, 'index.html', {'movies': movies})


def serie(request):
    series = Serie.objects.all()
    paginator = Paginator(series, 12) # 10 results per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'series.html', {'series': page_obj})


def movie(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 12) # 10 results per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
     
     
    return render(request, 'movies.html', {'movies': page_obj})

def movie_play(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    context = {
        'movie': movie,
    }
    return render(request, 'movie_play.html', context)

def serie_play(request, serie_id):
    serie = get_object_or_404(Serie, pk=serie_id)
    context = {
        'serie': serie
    }
    return render(request, 'serie_player.html', context)

def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        movies = Movie.objects.filter(Q(title__icontains=query) | Q(genre__icontains=query))
        series = Serie.objects.filter(Q(title__icontains=query) | Q(genres__icontains=query))
        results = list(chain(movies, series))

    paginator = Paginator(results, 12) # 10 items per page
    page = request.GET.get('page')
    results = paginator.get_page(page)
    context = {'results': results}
    
    return render(request, 'search.html', context)


