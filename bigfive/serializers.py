from rest_framework import serializers
from .models import Test

class TestSerializer(serializers.ModelSerializer):
    class Meta :
        model = Test
        fields = '__all__'

class SearchTestSerializer(serializers.ModelSerializer):
    # test = TestSerializer(source='test_set', many=True, read_only=True)
    class Meta : 
        model = Test
        fields = '__all__'

class SearchTestTypeSerializer(serializers.ModelSerializer):
    test = TestSerializer(source='user_set', many=True, read_only=True)
    class Meta : 
        model = Test
        fields = '__all__'