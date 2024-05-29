from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)

    def update(self, instance, validated_data):
        instance.password = make_password(validated_data.get('password', instance.password))
        return super().update(instance, validated_data)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name']
