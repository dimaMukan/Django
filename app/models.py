from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    feedback = models.TextField()
    rating = models.PositiveIntegerField()


class Customer(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    profile_pic = models.ImageField(default="1.png", null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name

class User1(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100,null=True,blank=True)
    e_mail = models.EmailField(null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    slug = models.SlugField(default='',db_index=True)

    # def save(self,*args,**kwargs):
    #     self.slug = slugify(self.name)
    #     super(User,self).save(*args,**kwargs)

    def get_url(self):
        return reverse('user-info', args=[self.slug])
