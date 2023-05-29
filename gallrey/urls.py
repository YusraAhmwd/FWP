from . import views
from django.urls import path

urlpatterns = [
path('product',views.product,name='product'),
path('country',views.Occasions,name='Occasions')


] 