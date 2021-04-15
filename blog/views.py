from django.shortcuts import render
from django.http import HttpResponse

"""
Create functions that handle what page the user is supposed to see when using any specific link.
For now we just return a simple httpresponse.
"""


def home(request):
    return HttpResponse('<h1>Blog Home</h1>')


def about(request):
    return HttpResponse('<h1>Blog About</h1>')
