from django.db import models
from django.conf import settings
from cart.models import CartItem

class Order(models.Model):
    user             = models.ForeignKey(settings.AUTH_USER_MODEL,
                                         on_delete=models.CASCADE)
    items            = models.ManyToManyField(CartItem)
    shipping_address = models.CharField(max_length=255)
    created          = models.DateTimeField(auto_now_add=True)
    paid             = models.BooleanField(default=False)

    def total(self):
        return sum(item.sub_total() for item in self.items.all())
