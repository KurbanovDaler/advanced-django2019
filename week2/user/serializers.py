from rest_framework import serializers
from user.models import Profile, MainUser
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('id', 'username')

    def create(self, validated_data):
        user = MainUser.objects.create_user(**validated_data)
        return user


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profile
