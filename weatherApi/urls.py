from django.urls import path, include
from .views import index
from .chartViews import chart

urlpatterns = [
    path("", index),
    path("data/", chart),
]
