from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator, MinValueValidator

class Movie(models.Model):

    Euro = 'EUR'
    Usd = 'USD'
    Uh = 'UKG'
    Currency = [
        (Euro, 'Euro'),
        (Usd, 'Dollar'),
        (Uh, 'Hrivna')
    ]

    currency = models.CharField(max_length=3,choices=Currency,default=Usd)
    name=models.CharField(max_length=40)
    rating=models.IntegerField(null=True,blank=True, validators=[MinValueValidator(1),MaxValueValidator(100)])
    slug = models.SlugField(default='',null=False,db_index=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args,**kwargs)


    def get_url(self):
        return reverse('info_one',args=[self.slug])

    def __str__(self):
        return f'{self.name} - {self.rating}'
