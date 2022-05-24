from unicodedata import name
from django.urls import path
from . import views
#http://127.0.0.1:8000 ==index
#http://127.0.0.1:8000/index ==index
#http://127.0.0.1:8000/blogs ==blogs
#http://127.0.0.1:8000/blogs/3 ==blogs-details


urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("countries", views.countries, name="countries"),
    path("years", views.years, name="years"),
    path("dataset", views.dataset, name="dataset"),
    path("correlation", views.correlation, name="correlation"),
    path("biggest", views.biggest, name="biggest"),

]