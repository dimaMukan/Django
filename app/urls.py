from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("feedback", views.feedback, name='feedback'),
    path("products", views.products, name='products'),
    path("food", views.food, name='food'),
    path("thx", views.thx, name='thx'),
    path('user/', views.userPage, name="user-page"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('account/', views.accountSettings, name="account"),

]