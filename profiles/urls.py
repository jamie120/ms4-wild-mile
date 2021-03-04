from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('saved_listings/', views.saved_listings, name='saved_listings'),
    path('my_listings/', views.my_listings, name='my_listings'),
    path('order_history/', views.order_history, name='order_history'),
    path('message_portal/', views.message_portal, name='message_portal')
]
