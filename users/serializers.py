from rest_framework import serializers
from .models import User, Position, Category


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    position = PositionSerializer(read_only=True)
    category = CategorySerializer(read_only=True)


class Meta:
    model = User
    fields = [
        'id', 'username', 'first_name', 'last_name',
        'phone_number', 'email', 'position', 'category',
    ]
