from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Product


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    created_at = serializers.DateField()
    price = serializers.IntegerField()
    class Meta:
        model = Product
        fields = '__all__'
