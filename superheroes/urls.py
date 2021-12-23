from django.urls import path
from superheroes import views

urlpatterns = [
    path('details/', views.superheroes.as_view())
]