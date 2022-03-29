from rest_framework import serializers
from .models import Employee
from django.contrib.auth.models import User


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def to_representation(self, instance):
        self.fields['employee'] = EmployeeSerializer(read_only=True)
        return super(CustomUserSerializer, self).to_representation(instance)
