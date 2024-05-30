from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from store.serializers import QuantitySerializer


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    user_quantity = QuantitySerializer(many=True, read_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = make_password(validated_data.pop('password'))
            instance.password = password
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'user_quantity']
