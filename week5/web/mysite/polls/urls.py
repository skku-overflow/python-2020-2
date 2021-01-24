from django.urls import path
from . import views

urlpatterns = [
    # https://docs.djangoproject.com/ko/3.1/intro/tutorial01/#path-argument-route
    path('', views.index, name='index'),
]
