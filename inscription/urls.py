from django.urls import path
from . import views

app_name = 'inscription'  # (Optionnel mais bien si tu veux utiliser le namespace)

urlpatterns = [
    path('', views.inscription, name='inscription'),
    path('confirmation/<str:reference_number>/', views.confirmation, name='confirmation'),
]
