from django.shortcuts import render



# Create your views here.
def home(requset):
    return render(requset,'page/home.html')

