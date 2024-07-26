# myapp/urls.py

from django.urls import path, include
from acervo import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('login/acervo/', views.acervo),
    path('login/acervo/emprestimo/', views.emprestimo),
    path('login/acervo/add/', views.acervo)
    # other URL patterns for your app
]
