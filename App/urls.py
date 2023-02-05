from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_like/<int:pk>', views.add_like, name='add_like'),
]