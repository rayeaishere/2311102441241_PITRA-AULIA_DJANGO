from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Category, Outfit, SavedOutfit

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class OutfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Outfit
        fields = '__all__'

class SavedOutfitSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavedOutfit
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
