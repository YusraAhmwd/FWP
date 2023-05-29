from django.shortcuts import render

# Create your views here.

def product(request):
    return render(request,'gallrey/product.html')

def Occasions(requst):
    return render(requst,'gallrey/Occasions.html')
