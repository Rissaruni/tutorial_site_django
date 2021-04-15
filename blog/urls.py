from django.urls import path
from . import views

"""
The project level urls.py solves paths up to '/blog' and leads here to process the the remaining parts.
Remmeber the the variable urlpatterns is a list, so separate elements properly.
"""

urlpatterns = [
    # views.home calls function we created in views.py
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
