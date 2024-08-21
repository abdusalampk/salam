from django.urls import path
from . import views
from .views import create_item, movie_output_view

urlpatterns = [
    path('sign/', views.sign,name='sign'),
    path('loginn/',views.loginn,name='loginn'),
    path('create_item/', create_item, name='create_item'),
    path('movies/', movie_output_view, name='movie_output_view'),



]
