from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_conversions, name='conversions'),
    path('<int:conversion_id>/', views.conversion_detail, name='conversion_detail'),
    path('save_listing/<int:conversion_id>&<conversion_unique_ref>/', views.save_listing, name='save_listing'),
    path('add/', views.add_conversion, name='add_conversion'),
    path('edit/<int:conversion_id>/', views.edit_conversion, name='edit_conversion'),
    path('delete/<int:conversion_id>/', views.delete_conversion, name='delete_conversion'),
    path('manage/', views.manage_conversions, name='manage_conversions'),
    path('approve/<conversion_id>', views.approve_conversion, name='approve_conversion'),
    path('delist/<conversion_id>', views.delist_conversion, name='delist_conversion'),
]
