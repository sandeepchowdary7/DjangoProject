from rest_framework import serializers
from .models import *
from djoser.serializers import UserCreateSerializer, UserSerializer


class BucketlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'user_name', 'email', 'password', 'first_name', 'last_name', 'phone')
