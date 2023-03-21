from django.db import models

# Create your models here.


class Slider(models.Model):
    title=models.CharField(blank=True,null=True,max_length=250)
    image=models.ImageField(upload_to='slider')
    date_added=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    


class Product(models.Model):
    category_choices = (
        ('Fruits','Fruits'),
          ('Vagetable','Vagetable'),
        ('Oil','Oil'),
        ('Rice','Rice'),
        ('Others','Others')

    )

    quantity_type_choices = (
        ('KG','KG'),
         ('Gram','Gram'),
        ('Ton','Ton'),
        ('Piece','Piece')

    )

    name=models.CharField(blank=True,null=True,max_length=200)
    description=models.TextField(blank=True,null=True)
    image=models.ImageField(upload_to='product',blank=True,null=True)
    price=models.IntegerField(blank=True,null=True)
    quantity=models.IntegerField(blank=True,null=True)
    quantity_type=models.CharField(max_length=60,choices=quantity_type_choices,blank=True,null=True)
    category=models.CharField(max_length=60,choices=category_choices,blank=True,null=True)
    is_approved=models.BooleanField(default=False)
    date_added=models.DateTimeField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.name