from django.urls import path, include
from .views import *


urlpatterns = [
    path("", produk_list, name='produk'),
    path("add_barang/", tambah_barang, name="add"),
    path("update_barang/<int:id>", update_barang, name="update"),
    path("delete_barang/<int:id>", delete_barang, name="delete")
]
