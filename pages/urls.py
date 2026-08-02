from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("another/", views.another_page, name="another"),
]
