from django.db import models



class Product(models.Model):
    title=models.CharField(max_length=150,default="Default Title")
    description=models.TextField(default="No description")
    price=models.DecimalField(decimal_places=2,max_digits=15,default=0.00)
    image=models.ImageField(upload_to="products/",default="products/default.jpg")
    time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
