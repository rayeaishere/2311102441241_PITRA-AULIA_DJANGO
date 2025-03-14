from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Category, Outfit, SavedOutfit
from .serializers import CategorySerializer, OutfitSerializer, SavedOutfitSerializer

# API untuk kategori fashion
class CategoryListCreateView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# API untuk outfit
class OutfitListCreateView(generics.ListCreateAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer

class OutfitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Outfit.objects.all()
    serializer_class = OutfitSerializer

# API untuk outfit yang disimpan pengguna
class SavedOutfitListCreateView(generics.ListCreateAPIView):
    queryset = SavedOutfit.objects.all()
    serializer_class = SavedOutfitSerializer
    permission_classes = [IsAuthenticated]  # Hanya user yang login yang bisa menyimpan outfit

class SavedOutfitDetailView(generics.RetrieveDestroyAPIView):
    queryset = SavedOutfit.objects.all()
    serializer_class = SavedOutfitSerializer
    permission_classes = [IsAuthenticated]
