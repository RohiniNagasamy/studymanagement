from django.urls import path
from . import views

urlpatterns = [
    path('', views.study_list, name='study_list'),
    path('add/', views.add_study, name='add_study'),
    path('view/<pk>/', views.view_study, name='view_study'),
    path('edit/<pk>/', views.edit_study, name='edit_study'),
    path('delete/<pk>/', views.delete_study, name='delete_study'),
]
