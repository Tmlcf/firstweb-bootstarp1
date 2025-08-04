
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('for/', views.for_view, name='for'),
]
