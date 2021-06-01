from django.urls import path
from . import views

urlpatterns = [
    path('', views.ytb_down, name='ybt_down'),
]
