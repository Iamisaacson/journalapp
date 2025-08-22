from django.urls import path
from . import views

urlpatterns = [
  path('favorite/', views.favorite, name='favorite')
]