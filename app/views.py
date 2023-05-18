from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from dataclasses import dataclass
# from .models import Movie
from django.db.models import Sum,Max,Min,Count
from .forms import FeedbackForm
from .models import Feedback

def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            feed = Feedback(
                name=form.cleaned_data['name'],
                surname=form.cleaned_data['surname'],
                feedback=form.cleaned_data['feedback'],
                rating=form.cleaned_data['rating'],
            )
            feed.save()
            return HttpResponseRedirect('/done')
    else:
        form = FeedbackForm()
    return render(request, 'app/feedback.html',context={'form':form})


def products(request):
    return render(request, 'app/products.html')

def food(request):
    return render(request, 'app/food.html')

def home(request):
    return render(request, 'app/home.html')

# # def get_info(request):
# #     movies = Movie.objects.order_by("-rating")
# #     agg = movies.aggregate(Sum('rating'))
# #     for movie in movies:
# #         movie.save()
# #
# #     return render(request,'app/info.html',{
# #         'movies':movies,
# #         'agg':agg,
# #     })
#
# def get_info_about_one(request,slug_movie:str):
#     movie = get_object_or_404(Movie,slug=slug_movie)
#     return render(request,'app/info_one.html',{
#         'movie':movie
#     })
