from django.db import models

# Create your models here.
class Book(models.Model):
    """Model for a book"""
    title=models.CharField(max_length=250)
    subtitle=models.CharField(max_length=250)
    author=models.CharField(max_length=100)
    isbn=models.CharField(max_length=13)

    def __str__(self):
        """display title in django admin"""
        return self.title