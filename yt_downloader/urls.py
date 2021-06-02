from django.urls import path
from . import views

urlpatterns = [
    path('ytb', views.ytb, name="ytb"),
]
