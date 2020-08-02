from django.urls import  path
from . import views

urlpatterns = [
    path("", views.index),
    # path("datachart",views.bar_chart())
]

