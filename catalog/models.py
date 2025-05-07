from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Outfit(models.Model):
    pilihan_kategori = [
        ('casual', 'Casual'),
        ('classy', 'Classy'),
        ('formal', ' Formal'),
        ('sporty', 'Sporty'),
        ('vintage', 'Vintage'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='outfits/')
    description = models.TextField(blank=True)
    category = models.CharField(max_length=20, choices=pilihan_kategori)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    