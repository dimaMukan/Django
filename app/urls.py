from django.urls import path, include
from . import views

urlpatterns = [
    # path("", views.hello, name='home'),
    path("hi/", views.name, name='hi'),
    # path("<int:num>", views.number),
    path("", views.get_info, name='info'),
    path("<slug:slug_movie>", views.get_info_about_one, name='info_one'),
]