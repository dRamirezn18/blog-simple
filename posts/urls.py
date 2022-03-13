from django import views
from django.urls import path
from . import views


app_name = "blog"
urlpatterns = [
    path("", views.blog, name="blog"),
    path("post/<str:pk>", views.post, name="post"),
]
