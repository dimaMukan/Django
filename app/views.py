from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from dataclasses import dataclass
from .models import Movie

def name(request):
    return HttpResponse("123")

@dataclass
class Person:
    name:str
    age:int

    def __str__(self):
        return f'This is {self.name}'


info_dict = {
    "one":"ONE!",
    "two":"TWO!",
    "three":"THREE!",
    "four":"FOUR!",
    "five":"FIVE!",
}

# def hello(request):
#     numbers = list(info_dict)
#     context = {
#         'numbers':numbers
#     }
#     return render(request,'app/test.html',context=context)

def get_info(request):
    movies = Movie.objects.all()
    return render(request,'app/info.html',{
        'movies':movies
    })

def get_info_about_one(request,id_movie:int):
    movies = Movie.objects.all()
    return render(request,'app/info.html',{
        'movies':movies
    })

#
# def number(request, num:int):
#     numbers = list(info_dict)
#     if num > len(numbers):
#         return HttpResponseNotFound(f"NOT FOUND! - {num}")
#     res = numbers[num - 1]
#     a = reverse('info',args=(res,))
#     return HttpResponseRedirect(a)
