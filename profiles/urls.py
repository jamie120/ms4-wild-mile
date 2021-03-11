from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('saved_listings/', views.saved_listings, name='saved_listings'),
    path('remove_saved_listing/<conversion_id>', views.remove_saved_listing, name='remove_saved_listing'),
    path('my_listings/', views.my_listings, name='my_listings'),
    path('view_order_history/', views.view_order_history, name='view_order_history'),
    path('order_history/<order_number>', views.order_history, name='order_history'),
    path('message_portal/', views.message_portal, name='message_portal')
]
