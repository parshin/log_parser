from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


def index(request):
    return HttpResponse("Hello! It works!")
