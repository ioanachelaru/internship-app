from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from application.models import Student, Hr
User._meta.get_field('email')._unique = True


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'username', 'email', 'password', 'name', 'cv')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        Student.objects.create(
            user=user, 
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data['name'], 
            email=validated_data['email'],
            cv=validated_data['cv'])
        return user

class HR_RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hr
        fields = ('id', 'username', 'email', 'password', 'name')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        Hr.objects.create(
            user=user, 
            username=validated_data['username'],
            password=validated_data['password'],
            name=validated_data['name'], 
            email=validated_data['email'])
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials!")