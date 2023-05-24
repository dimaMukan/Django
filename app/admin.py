from django.contrib import admin, messages
from .models import Customer,User1
from django.db.models import QuerySet, Q

admin.site.register(Customer)


@admin.register(User1)
class UserAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'last_name','age', 'city', 'e_mail', 'password', 'slug']
    list_editable = ['age','city','e_mail', 'password', 'slug']
    ordering = ['-name']
    list_filter = ['name']
