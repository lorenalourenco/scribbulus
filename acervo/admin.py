from django.contrib import admin

from .models import Product, Author, Genre, ProductInstance
from django.db.models.functions import Lower


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre', 'status')

class ProductInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','Product','imprint','due_back','status')

admin.site.register(Author)
admin.site.register(ProductInstance)
admin.site.register(Product)
admin.site.register(Genre)