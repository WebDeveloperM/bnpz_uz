from django.urls import path
from .views import index, chronicle, politics, leader

urlpatterns = [
    path("", index, name='index'),
    path("chronicle/", chronicle, name="chronicle"),
    path("politics/", politics, name="politics"),
    path("leader/", leader, name="leader"),
]