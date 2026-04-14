from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
   
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    price = models.FloatField()
    old_price = models.FloatField()

    def discount(self):
        return int(self.old_price - self.price)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='books/')
    description = models.TextField()

    is_offer = models.BooleanField(default=False)
    is_kids = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    is_best_seller = models.BooleanField(default=False)
    is_anime = models.BooleanField(default=False)
    is_pack = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    qty = models.IntegerField(default=1)

    def subtotal(self):
        return self.book.price * self.qty


