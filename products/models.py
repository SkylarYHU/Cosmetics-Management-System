from django.db import models


# Create your models here.
class Product(models.Model):
  CATAGORY_CHOICES = [
    ('skincare', '护肤品'),
    ('makeup', '彩妆'),
    ('haircare', '护发品'),
  ]

  name = models.CharField(max_length=100)
  category = models.CharField(max_length=50, choices=CATAGORY_CHOICES)
  ingredients = models.TextField()
  benefits = models.TextField()
  price = models.DecimalField(max_digits=10, decimal_places=2)
  stock = models.IntegerField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.name