from django.urls import path
from .import views

urlpatterns = [
    path('order/', views.checkout, name='order'),
    path('orderconfrmation/', views.orderconf, name='orderconf')
]
