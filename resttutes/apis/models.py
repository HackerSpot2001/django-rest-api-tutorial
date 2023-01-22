from django.db import models

# Create your models here.
class Product(models.Model):
    pid = models.BigAutoField(primary_key=True,unique=True)
    name = models.CharField(max_length=100,null=False)
    desc = models.CharField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True)


    class Meta:
        ordering = ['date_created']