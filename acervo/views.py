from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .models import Product

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Obtém o username do formulário
        password = request.POST.get('password')  # Obtém a senha do formulário
        useruser = authenticate(request, username=username, password=password)
        print(useruser)
        try:
            login(request, useruser)
            # Redireciona para uma página de sucesso.
            return redirect('acervo/')
        except Exception as e:
            raise(request, 'login.html', {'error_message': e})
    else:
        return render(request, 'login.html')
    
def index(request):
    products = Product.objects.all()
    return render(request, 'acervo.html', {'products': products})

def index2(request):
    instance = ProductInstance.objects.get(pk=1)
    return render(request, 'acervo.html', {'instance': instance})
