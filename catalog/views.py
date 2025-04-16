from django.shortcuts import render
from .models import Outfit, Category
# Create your views here.
def list_outfit(request):
    categories = Category.objects.all()
    outfits = Outfit.objects.all()
    return render(request, 'catalog/outfits.html', {
        'categories': categories,
        'outfits': outfits
    })