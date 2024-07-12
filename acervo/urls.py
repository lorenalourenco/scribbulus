# myapp/urls.py

from django.urls import path, include
from acervo import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('login/acervo/', views.index),
    # other URL patterns for your app
]
