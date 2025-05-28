from django.db import models

# Create your models here.
class Post(models.Model):
    judul = models.CharField(max_length=200)
    isi = models.TextField()
    image = models.ImageField(upload_to='blog_images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.judul
    
class Komen(models.Model):
    post = models.ForeignKey(Post, related_name='komen', on_delete=models.CASCADE)
    nama = models.CharField(max_length=100)
    isi = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'dikomentari oleh {self.nama}'