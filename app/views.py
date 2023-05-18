from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from dataclasses import dataclass
# from .models import Movie
from django.db.models import Sum,Max,Min,Count
from .forms import FeedbackForm
from .models import Feedback, Customer
from .forms import CreateUserForm, CustomerForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

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
            return HttpResponseRedirect('/thx')
    else:
        form = FeedbackForm()
    return render(request, 'app/feedback.html',context={'form':form})
def thx(request):
    return render(request, 'app/thx.html')
def products(request):
    return render(request, 'app/products.html')
def food(request):
    return render(request, 'app/food.html')
def home(request):
    return render(request, 'app/home.html')





def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='customer')
            user.groups.add(group)

            Customer.objects.create(
                user=user,
                name=user.username,
            )
            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'app/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request,'username OR password is incorrect')
    context = {}
    return render(request, 'app/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')


def userPage(request):
    context = {}
    return render(request, 'app/user.html', context)

def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance=customer)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'app/account_settings.html', context)
