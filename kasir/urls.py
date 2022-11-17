from django.contrib import admin
from django.urls import path, include
from .views import *


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", dashboard, name='home'),
    path("about/", about, name='about'),
    # apps urls here
    path('produk/', include('produk.urls'))
]
