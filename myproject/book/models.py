from django.db import models
from django.urls import reverse

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    publisher = models.CharField(max_length=50)
    publication_date = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('book:list')