from django import forms 
from .models import Product , Category,Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category','image','title','discription','price','brand']
        
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title']
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['content','rating']