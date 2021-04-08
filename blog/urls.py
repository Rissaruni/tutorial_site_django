from django.urls import path
from . import views

urlpatterns = [
    # views.home calls function we created in views.py
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
