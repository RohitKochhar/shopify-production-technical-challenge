# --------------------------------------------------------
# File Name: tracker/urls.py
#
# File Description: This file is used to map views to URLs
# 
# --------------------------------------------------------

# Imports ------------------------------------------------
from django.urls import path

from . import views

# Global variables ---------------------------------------
app_name = 'tracker'

urlpatterns = [
    path("", views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('export/', views.export, name='export')
]