from django.contrib import admin
from django.urls import path, include
from .views import ForwardListView, ForwardUpdateView

app_name = 'appmulti'

urlpatterns = [
    path('', ForwardListView.as_view(), name='forward_list'),
    path('forward/<int:pk>/edit', ForwardUpdateView.as_view(), name='edit_forward'),
]
