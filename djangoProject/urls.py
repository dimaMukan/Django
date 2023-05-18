from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Our admin'
admin.site.index_title = 'Super admin'

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("app.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
]
