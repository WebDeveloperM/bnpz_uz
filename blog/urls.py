from django.urls import path
from .views import index, chronicle, politics, leader, leader_detail, product

urlpatterns = [
    path("", index, name='index'),
    path("chronicle/", chronicle, name="chronicle"),
    path("politics/", politics, name="politics"),
    path("leader/", leader, name="leader"),
    path("leader/<int:pk>", leader_detail, name="leader_detail"),
    path("product", product, name="product"),
]