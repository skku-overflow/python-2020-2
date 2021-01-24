from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    """
    메인 페이지
    """
    return HttpResponse("Hello, world. You're at the polls index.")
