from audioop import reverse
from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse
from category.models import Category
# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = RichTextField()
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    image_1 = models.ImageField(upload_to='photos/products', blank=True)
    image_2 = models.ImageField(upload_to='photos/products', blank=True)
    image_3 = models.ImageField(upload_to='photos/products', blank=True)
    image_4 = models.ImageField(upload_to='photos/products', blank=True)
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name