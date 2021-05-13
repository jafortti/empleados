from django.urls import path
from .views import (
    PruebaView,
    PruebaListView,
    ListarPruebaListView,
    PruebaCreateView,
     ResumeFoundationView
)


urlpatterns = [
    path('prueba/',PruebaView.as_view()),
    path('lista/',PruebaListView.as_view()),
    path('lista-prueba/',ListarPruebaListView.as_view()),
    path('add/',PruebaCreateView.as_view()),
    path('resume-foundation/', ResumeFoundationView.as_view(),name='resume-foundation'),
]