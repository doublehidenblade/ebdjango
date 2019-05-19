from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('members', views.members , name="members"),
    path('shorts', views.shorts, name="shorts"),
    path('activities', views.activities, name="activities"),
]
