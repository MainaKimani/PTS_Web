from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('',views.overview),
    path('projects/',views.projects),
    path('cohort/',views.cohort)
]
