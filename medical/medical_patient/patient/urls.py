from django.urls import path
from .views import *

urlpatterns = [
    path('', menu, name='menu'),
    path('createuser/', create, name='create'),
    path('searchuser/', search, name='search'),
    path('information/', information, name='information')
]