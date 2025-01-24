from django.db import models
from django.contrib.auth.models import User
from products.models import Product

# Create your models here.

class sabad(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    paid=models.BooleanField(default=False,verbose_name='پرداخت شده / نشده')
    pay_date=models.DateTimeField(blank=True,null=True)


    class Meta:
        verbose_name='سبد خرید'
        verbose_name_plural='سبدهای خرید'

    def __str__(self):
        return self.user.get_full_name()



class sabad_detail(models.Model):
    order=models.ForeignKey(sabad,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    count=models.IntegerField(default=0)
    price=models.IntegerField(default=0)

    class Meta:
        verbose_name='جزئیات سبد خرید'
        verbose_name_plural='جزئیات سبدهای خرید'

    def __str__(self):
        return self.product.title
