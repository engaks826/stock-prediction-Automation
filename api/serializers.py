from django.contrib.auth.models import User
from rest_framework import serializers
from dataentry.models import Student, Employee, Blog, Comment



class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        # user = User.objects.create_user(**validated_data)
        return user


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Student
        fields='__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Employee
        fields='__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Comment
        fields='__all__'

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model= Blog
        fields='__all__'


