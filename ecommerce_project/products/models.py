from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    category    = models.ForeignKey(Category,
                                    on_delete=models.CASCADE,
                                    related_name='products')
    name        = models.CharField(max_length=200)
    slug        = models.SlugField(max_length=200, unique=True)
    image       = models.ImageField(upload_to='products/')
    description = models.TextField(blank=True)
    price       = models.DecimalField(max_digits=10, decimal_places=2)
    available   = models.BooleanField(default=True)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.name

