from rest_framework import serializers
from quizz_app.models import Quiz, Question

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_title', 'question_options', 'answer', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
    
    def validate_question_options(self, value):
        if not isinstance(value, list):
            raise serializers.ValidationError('question_options must be a list.')
        if len(value) != 4:
            raise serializers.ValidationError('A question must have exactly 4 options.')
        return value 
    
    def validate(self, data):
        options = data.get('question_options')
        answer = data.get('answer')
        if options and answer and answer not in options:
            raise serializers.ValidationError({'answer': 'Answer must be one of the question_options.' })
        return data
        
        
class QuizSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Quiz
        fields = ['id', 'owner', 'title', 'description', 'video_url', 'created_at', 'updated_at', 'questions']

