from rest_framework import serializers
from .models import User, Position, EmployeeCategory


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class EmployeeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeCategory
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    position = PositionSerializer(read_only=True)
    employee_category = EmployeeCategorySerializer(read_only=True)


class Meta:
    model = User
    fields = [
        'id', 'username', 'first_name', 'last_name',
        'phone_number', 'email', 'position', 'employee_category',
    ]
