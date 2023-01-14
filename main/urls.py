from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('Demand', views.demand, name='demand'),
    path('Geography', views.geo, name='geo'),
    path('Skills', views.skills, name='skills'),
    path('Last-vacancies', views.last, name='last-vacs')
]
