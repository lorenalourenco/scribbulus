from django.db import models
import uuid
from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    # Optionally, add custom validation or fields here
    pass



class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a book genre (e.g. Science Fiction)')

    def __str__(self):
        return self.name
    
class Product (models.Model): #BOOK
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=1000)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2000)
    genre = models.ManyToManyField(Genre, )

    LOAN_STATUS = (
        ('Maintenance', 'Maintenance'),
        ('On Loan', 'On loan'),
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
    )
    status = models.CharField(
        max_length=100,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
    
    def display_genre(self):
        return ', '.join(genre.name for genre in self.genre.all()[:3])

    display_genre.short_description = 'Genre'

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
    
class ProductInstance(models.Model):
    """Model representing a specific copy of a book (i.e. that can be borrowed from the library)."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular book across whole library')
    Product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('Maintenance', 'Maintenance'),
        ('On Loan', 'On loan'),
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
    )

    status = models.CharField(
        max_length=100,
        choices=LOAN_STATUS,
        blank=True,
        default='m',
        help_text='Book availability',
    )

