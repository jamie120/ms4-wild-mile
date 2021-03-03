from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_conversions, name='conversions'),
    path('<int:conversion_id>/', views.conversion_detail, name='conversion_detail'),
    path('add/', views.add_conversion, name='add_conversion'),
    path('approve/', views.approve_conversions, name='approve_conversions'),
    path('approve/<conversion_id>', views.approve_conversion, name='approve_conversion'),
]
