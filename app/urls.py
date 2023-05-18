from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("feedback", views.feedback, name='feedback'),
    path("products", views.products, name='products'),
    path("food", views.food, name='food'),

]