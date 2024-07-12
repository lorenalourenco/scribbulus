from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('acervo.html')
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error_message': 'Invalid credentials.'})
    else:
        return render(request, 'login.html')

def index(request):
    products = Product.objects.all()
    return render(request, 'acervo.html', {'products': products})

def index2(request):
    instance = ProductInstance.objects.get(pk=1)
    return render(request, 'acervo.html', {'instance': instance})
