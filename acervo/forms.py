from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from django.forms import ModelForm
from .models import *

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

    
class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'



class ProductInstanceForm(forms.ModelForm):
    class Meta:
        model = ProductInstance
        fields = '__all__'


class ArticleForm(ModelForm):
    class Meta:
        error_messages = {
            NON_FIELD_ERRORS: {
                "unique_together": "%(model_name)s's %(field_labels)s are not unique.",
            }
        }