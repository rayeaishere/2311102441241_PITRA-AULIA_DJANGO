from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    url = models.URLField()
    urlToImage = models.URLField(blank=True, null=True)
    published_at = models.DateTimeField()

    def __str__(self):
        return self.title