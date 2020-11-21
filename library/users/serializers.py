from django.contrib.auth.models import User, Group
from rest_framework import serializers



class UserSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializers for User Model
    """

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True, 'required': True}}


    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user