from django.db import models
from django.contrib.auth.models import User

# Model untuk kategori fashion
class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name

# Model untuk outfit
class Outfit(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='outfits/')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    season = models.CharField(
        max_length=20,
        choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Fall', 'Fall'), ('Winter', 'Winter')]
    )
    colors = models.CharField(max_length=255, help_text='Comma-separated colors')
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

# Model untuk menyimpan outfit favorit pengguna
class SavedOutfit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    outfit = models.ForeignKey(Outfit, on_delete=models.CASCADE)
    saved_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('user', 'outfit')
    
    def __str__(self):
        return f"{self.user.username} saved {self.outfit.title}"

# Ensure all dependencies are installed
try:
    import micropip
except ModuleNotFoundError:
    raise ModuleNotFoundError("The 'micropip' module is missing. Please install it using 'pip install micropip'.")
