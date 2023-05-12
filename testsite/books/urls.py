
from django.urls import path

from .views import *
from . import views

urlpatterns = [
    path('', index, name='home'),
    path('<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('stats/', stats, name='stats'),
    path('create/', create, name='create'),




]


