from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_conversions, name='conversions'),
    path('<conversion_id>', views.conversion_detail, name='conversion_detail'),
]
