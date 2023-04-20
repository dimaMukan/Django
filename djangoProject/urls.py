from django.contrib import admin
from django.urls import path, include
# from app.views import name

urlpatterns = [
    path("admin/", admin.site.urls),
    path("app/", include("app.urls")),
    path('__debug__/', include('debug_toolbar.urls')),
]
