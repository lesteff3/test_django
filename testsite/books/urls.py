
from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('stats/', stats, name='stats'),
    path('create/', create, name='create')


]


