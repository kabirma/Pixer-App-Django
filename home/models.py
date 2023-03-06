from django.db import models
from django.conf import settings
# Create your models here.
class BlogCategory(models.Model):
    name=models.CharField( max_length=150)
    created_at=models.DateField(  auto_now_add=True)
    updated_at = models.DateField( auto_now=True)


class Blog(models.Model):
    name =models.CharField( max_length=250)
    category = models.ForeignKey("BlogCategory", on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    image = models.ImageField( upload_to="images/",blank=True,null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)
    created_at = models.DateField( auto_now_add=True)
    updated_at = models.DateField( auto_now=True)