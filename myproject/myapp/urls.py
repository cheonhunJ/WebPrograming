from django.urls import path
from . import views
from .views import map_view

urlpatterns = [
    path('', views.home, name='home'),

    path('login/',views.login, name='login'),

    path('busmap/', views.busmap, name='busmap'),


    path('map/', views.map_view, name='map'),

    path('info/', views.info, name='info'),

]
