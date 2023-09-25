from django.urls import path
from . import views

urlpatterns = [
    path('oc/', views.index, name='onboardcomputer'),
    path('upload/', views.upload_file, name='upload'),
]