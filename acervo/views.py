from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Product, Genre, Author, ProductInstance
from .forms import GenreForm, AuthorForm, ProductForm, ProductInstanceForm, forms

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
           return redirect('acervo/')
    else:
        return render(request, 'login.html')
    

def acervo(request):
    if request.method == 'POST':
        # Criação dos formulários com dados POST
        genre_form = GenreForm(request.POST)
        author_form = AuthorForm(request.POST)
        product_instance_form = ProductInstanceForm(request.POST)
        product_form = ProductForm(request.POST)
        
        # Verificação da validade dos formulários
        if (genre_form.is_valid() and
            author_form.is_valid() and
            product_instance_form.is_valid() and
            product_form.is_valid()):
            
            # Salvar os dados dos formulários
            product = product_form.save()
            product_instance = product_instance_form.save(commit=False)
            product_instance.product = product  # Ajuste se necessário
            product_instance.save()
            
            # Redirecionar após o salvamento
            return redirect('acervo')  # Redireciona para a mesma página ou para uma página de sucesso
    
    else:
        # Criação dos formulários vazios para uma requisição GET
        genre_form = GenreForm()
        author_form = AuthorForm()
        product_instance_form = ProductInstanceForm()
        product_form = ProductForm()
    
    # Contexto para o template
    forms = {
        'genre_form': genre_form,
        'author_form': author_form,
        'product_instance_form': product_instance_form,
        'product_form': product_form
    }
    products = Product.objects.all()
    return render(request, 'acervo.html', {'products': products, 'forms': forms})

def instance(request):
    instance = ProductInstance.objects.get(pk=1)
    return render(request, 'acervo.html', {'instance': instance})

def emprestimo(request):
    return render(request, 'emprestimo.html', {'products': Product})

def addauthor(request):
    if request.method == "POST":
        forms = AuthorForm(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('http://127.0.0.1:8000/login/acervo/formulariolivro') 
    else:
        forms = AuthorForm()
        return render(request, 'formulariolivro.html', {'forms': forms})

def manage_products(request):
    forms = ProductForm(request.POST)

    if request.method == "POST":
        if 'delete_product' in request.POST:
            product_id = request.POST.get('product_id')
            if product_id:
                product = get_object_or_404(Product, id=product_id)
                product.delete()
            return redirect('http://127.0.0.1:8000/login/acervo/formulariolivro')  # Redireciona para evitar reenvio do formulário

        elif 'add_product' in request.POST:
            forms = ProductForm(request.POST)
            if forms.is_valid():
                forms.save()


    else:
        forms = ProductForm()
    
    products = Product.objects.all()
    return render(request, 'formulariolivro.html', {'products': products, 'forms': forms})


