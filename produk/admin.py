from django.contrib import admin
from .models import *

# Register your models here.

class AdminProduk(admin.ModelAdmin):
    list_display = ['nama', 'deskripsi', 'jumlah', 'kategori']

admin.site.register(Kategori)
admin.site.register(Circle_produk, AdminProduk)