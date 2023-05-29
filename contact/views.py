from django.shortcuts import render
from .models import Con
from django.http import HttpResponse 

# Create your views here.
def index(requset):
  
    if requset.method=="POST":
         
         contact=Con()
         
         firstname=requset.POST.get('firstname')
         Subject=requset.POST.get('Subject')
         email=requset.POST.get('email')
         Con.firstname=firstname
         Con.Subject=Subject
         Con.email=email
         
         Con.save()
         return HttpResponse("<h1>Thank you for contact us</h1>")
        
    return render(requset,'contact/contact.html')
    
    