from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Outfit

def list_outfit(request):
    category = request.GET.get('category')
    outfits = Outfit.objects.all()
    
    if category:
        outfits = outfits.filter(category__iexact=category)

    paginator = Paginator(outfits, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Outfit.objects.values_list('category', flat=True).distinct()

    return render(request, 'catalog/outfits.html', {'outfits': outfits})

def home(request):
    return render(request, 'home/index.html')