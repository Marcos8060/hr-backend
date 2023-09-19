from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import *
    

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class PermissionSerializer(serializers.ModelSerializer):
    role_name = serializers.SerializerMethodField()

    class Meta:
        model = Permission
        # fields = '__all__'
        fields = ['id', 'permission','role_name']

    def get_role_name(self, obj):
        return obj.role.name



class AllPermissionsSerializer(serializers.ModelSerializer):
    role_name = serializers.SerializerMethodField()
    class Meta:
        model = Permission
        fields = ['id', 'permission','role_name']
    
    def get_role_name(self, obj):
        return obj.role.name
    

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    role = serializers.CharField()  # Accept role as a string

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        # Extract and remove the 'role' string from the validated data
        role_name = validated_data.pop('role')

        # Find or create the corresponding Role object
        role, _ = Role.objects.get_or_create(name=role_name)

        # Assign the Role object back to the 'role' field
        validated_data['role'] = role

        password = validated_data.pop('password')
        user = Employee.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


