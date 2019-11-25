from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta :
        model = User
        fields = '__all__'

class SearchUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='user_set', many=True, read_only=True)
    class Meta : 
        model = User
        fields = '__all__'