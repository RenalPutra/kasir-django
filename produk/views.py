from multiprocessing import context
from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def produk_list(request):
    template_name = "produk_list.html"
    group_produk = Circle_produk.objects.all()
    context ={
        "produk" : group_produk,
    }
    return render(request, template_name, context)

def tambah_barang(request):
    template_name = "add_barang.html"
    kategori = Kategori.objects.all()
    if request.method == "POST":
        input_nama = request.POST.get('nama')   
        input_jumlah = request.POST.get('jumlah')   
        input_deskripsi = request.POST.get('deskripsi')   
        input_kategori = request.POST.get('kategori')
        
        get_kategori = Kategori.objects.get(nama=input_kategori)   
        
        Circle_produk.objects.create(
            nama = input_nama,
            jumlah = input_jumlah,
            deskripsi = input_deskripsi,
            kategori = get_kategori
        )
        return redirect(produk_list)
    context ={
        "kategori": kategori
    }   
    
    return render(request, template_name, context)

def update_barang(request,id):
    template_name = "add_barang.html"
    kategori = Kategori.objects.all()
    get_produk = Circle_produk.objects.get(id=id)
    if request.method == "POST":
        input_nama = request.POST.get('nama')   
        input_jumlah = request.POST.get('jumlah')   
        input_deskripsi = request.POST.get('deskripsi')   
        input_kategori = request.POST.get('kategori')
        
        get_kategori = Kategori.objects.get(nama=input_kategori)   
        get_produk.nama = input_nama
        get_produk.jumlah = input_jumlah
        get_produk.deskripsi = input_deskripsi
        get_produk.kategori = get_kategori
        get_produk.save()
        return redirect(produk_list)
    
    
    context ={
        "kategori": kategori,
        "get_produk" : get_produk
    }   
    
    return render(request, template_name, context)

def delete_barang(request, id):
    Circle_produk.objects.get(id=id).delete()
    return redirect(produk_list)