from django.urls import path

from . import views

urlpatterns = [
    path('messenger/', views.messenger),
    path('<str:room_name>/', views.room, name='room'),
]