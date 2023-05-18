from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Customer


class FeedbackForm(forms.Form):
    name = forms.CharField(label='Name',max_length=20,min_length=2)
    surname = forms.CharField(label='Surname',max_length=50,min_length=2)
    feedback = forms.CharField(label='Feedback',max_length=50,min_length=2,widget=forms.Textarea(attrs={'rows':4,'cols':20}))
    rating = forms.IntegerField(label='Rating',min_value=1,max_value=5)


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
