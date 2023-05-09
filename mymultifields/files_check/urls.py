from django.contrib import admin
from django.urls import path, include
from .views import MainPage, model_form_upload, take_files_two

app_name = 'file_check'

urlpatterns = [
    path('main/', MainPage.as_view(), name='index'),
    path('upload/', model_form_upload, name='upload'),
    path('check/<int:pk>/', take_files_two, name='check'),
]
