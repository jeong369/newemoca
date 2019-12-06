from rest_framework import serializers
from .models import Test, Score

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

class SearchUserTestSerializer(serializers.ModelSerializer):
    test = TestSerializer(source='user_set', many=True, read_only=True)
    resultscore = serializers.IntegerField()
    class Meta : 
        model = Test
        fields = ['label', 'facet', 'question', 'question_ko', 'key', 'testname', 'resultscore']

class ScoreSerializer(serializers.ModelSerializer):
    class Meta :
        model = Score
        fields = ('grade',)