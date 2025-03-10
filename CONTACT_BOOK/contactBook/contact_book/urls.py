from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('add/', views.add_contact, name='add_contact'),
    path('edit/<int:contact_id>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:contact_id>', views.delete_contact, name='delete_contact'),
    path('search/', views.search, name='search'),
]