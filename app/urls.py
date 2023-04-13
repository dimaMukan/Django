from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.hello),
    path("hi/", views.name, name='hi'),
    path("<int:num>", views.number),
    path("<str:info>", views.get_info, name='info'),
]