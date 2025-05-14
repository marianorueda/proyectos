from django.urls import path
from . import views  

urlpatterns = [
    path('', views.index, name='index'),
    path('options/', views.options, name='options'),
    path('registerPackage/', views.registerPackage, name='registerPackage'),
    path('selectTransport/', views.selectTransport, name='selectTransport'),
    path('transportArrival/', views.transportArrival, name='transportArrival'),
    path('message/', views.message, name='message'),
]