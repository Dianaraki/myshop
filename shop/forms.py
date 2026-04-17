from django import forms
from .models import Category, Product, Review

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']
        labels = {
            'name': 'Санат атауы',
            'description': 'Сипаттамасы',
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'title', 'price', 'is_available']
        labels = {
            'category': 'Санаты',
            'title': 'Тауар атауы',
            'price': 'Бағасы',
            'is_available': 'Қолжетімде ме?',
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author', 'rating', 'text']
        labels = {
            'author': 'Сіздің есіміңіз',
            'rating': 'Бағаңыз (1-5)',
            'text': 'Пікіріңіз',
        }
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'text': forms.Textarea(attrs={'rows': 4}),
        }