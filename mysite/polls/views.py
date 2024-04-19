from django.shortcuts import render
from django.http import HttpResponse
from .models import cache


def index(request):
    record = {
        "teste" : 0
    }
    cache.insert_one(record)
    return HttpResponse("Hello, world. You're at the polls index.")

