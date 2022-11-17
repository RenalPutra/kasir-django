from django.http import HttpResponse
from django.shortcuts import render

def dashboard(request):
    template_name = "main.html"
    return render(request, template_name)
def about(request):
    template_name = "about.html"
    return render(request, template_name)