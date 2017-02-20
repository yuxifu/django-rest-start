"""
Serializers for Admin views
"""
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class SignUpSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        # make password write-only
        extra_kwargs = {'password': {'write_only': True}}


class OAuth2PasswordAccessTokenRequestFields(object):

    def __init__(self, client_id="", client_secret="",
                 username="", password=""):
        self.granyt_type = 'password'
        self.client_id = client_id
        self.client_secret = client_secret
        self.username = username
        self.password = password


class OAuth2PasswordAccessTokenRequestFieldsSerializer(serializers.Serializer):
    grant_type = serializers.CharField(max_length=256, default='password')
    client_id = serializers.CharField(max_length=256)
    client_secret = serializers.CharField(max_length=256, required=False)
    username = serializers.CharField(max_length=256)
    password = serializers.CharField(max_length=256)

    def update(self, instance, validated_data):
        instance.grant_type = validated_data.get(
            'grant_type', instance.grant_type)
        instance.client_id = validated_data.get(
            'client_id', instance.client_id)
        instance.client_secret = validated_data.get(
            'client_secret', instance.client_secret)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        return instance

    def create(self, validated_data):
        return OAuth2PasswordAccessTokenRequestFields(**validated_data)
