from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_conversions, name='conversions'),
    path('<int:conversion_id>/', views.conversion_detail, name='conversion_detail'),
    path('save_listing/<int:conversion_id>/', views.save_listing, name='save_listing'),
    path('add/', views.add_conversion, name='add_conversion'),
    path('edit/<int:conversion_id>/', views.edit_conversion, name='edit_conversion'),
    path('approve/', views.approve_conversions, name='approve_conversions'),
    path('approve/<conversion_id>', views.approve_conversion, name='approve_conversion'),
]
