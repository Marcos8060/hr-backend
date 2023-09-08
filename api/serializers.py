from rest_framework import serializers
from .models import User,Project,Permission
    

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



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
        # eliminate the password from being return upon user registration.
        extra_kwargs = {
            'password' : { 'write_only': True}
        }


   # hash the user password in the database
    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


