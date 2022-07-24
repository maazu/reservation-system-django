from django.urls import path

from .views import ClientListView,ClientReterive

urlpatterns = [
    path('',  ClientListView.as_view(), name='clients-list'),
    path('<int:pk>/',  ClientReterive.as_view(), name='clients-list'),
]