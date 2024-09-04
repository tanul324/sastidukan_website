from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length = 100)
    
    slug = models.SlugField(max_length = 100 , blank=True)
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Category,self).save(*args,**kwargs)


class Product(models.Model):
    title = models.CharField(max_length = 150, help_text="enter product name")
    price= models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(help_text="enter product description")
    image = models.ImageField(upload_to="product")
    
    slug = models.SlugField(max_length = 150, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    seller= models.ForeignKey(User, on_delete=models.CASCADE)
    brand = models.CharField(max_length = 100)
    created_at = models.DateTimeField( auto_now_add=True)
    
    
    def __str__(self):
        return self.title
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(Product,self).save(*args,**kwargs)
        
class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    rating = models.IntegerField()
    created_at = models.DateTimeField( auto_now_add=True)
    
    def __str__(self):
        return f"{self.product.title} review by {self.customer.username}"
    
    
    
    
    



    
    
    
    
