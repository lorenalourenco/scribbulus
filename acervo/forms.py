from django import forms
from .models import *

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

    
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


class ProductInstanceForm(forms.ModelForm):
    class Meta:
        model = ProductInstance
        fields = '__all__'


