from rest_framework import serializers
from .models import Info

class InfoSerializer(serializers.ModelSerializer):
    class Meta :
        model = Info
        fields = '__all__'

class SearchInfoSerializer(serializers.ModelSerializer):
    info = InfoSerializer(source='info_set', many=True, read_only=True)
    class Meta : 
        model = Info
        fields = '__all__'