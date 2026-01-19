from rest_framework import serializers
from quizz_app.api.utils import generate_quiz_from_youtube
from quizz_app.models import Quiz, Question

class QuestionSerializer(serializers.ModelSerializer):
    '''
    Serializer for quiz questions. 
    '''
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
    '''
    Serializer for listing quizzes.
    
    '''
    questions = QuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Quiz
        fields = ['id', 'owner', 'title', 'description', 'video_url', 'created_at', 'updated_at', 'questions']

class QuizDetailSerializer(serializers.ModelSerializer):
    '''
    Serializer for detailed view of a quiz.
    Allows updating title and description only.
    
    '''
    
    questions = QuestionSerializer(many=True, read_only=True)
    
    class Meta:
        model = Quiz
        fields = [  'id',  'owner',  'title',  'description',  'video_url',  'created_at',  'updated_at',  'questions']
        read_only_fields = [  'id',  'owner',  'video_url',  'created_at',  'updated_at',  'questions']

    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance
    

class QuizAIGenerateCreateSerializer(serializers.Serializer):
    '''
    Serializer to handle quiz generation from a YouTube video URL.
    
    '''
    url = serializers.CharField()
    
    class Meta:
        fields = ['url']
        
    def create(self, validated_data):
        request = self.context['request']
        user = request.user
        video_url = validated_data['url']
        
        result =generate_quiz_from_youtube(video_url) 
        
        if not result['success']:
            raise serializers.ValidationError({'error': 'Failed to generate quiz: ' , 'details': result.get('error', 'Unknown error')})
        
        quiz_data = result['quiz']
        
        quiz = Quiz.objects.create(
            owner=user,
            title=quiz_data['title'],
            description=quiz_data['description'],
            video_url=video_url
        )
        for question_data in quiz_data.get('questions', []):
            question = Question(
                quiz=quiz,
                question_title=question_data.get('question_title', ''),
                question_options=question_data.get('question_options', []),
                answer=question_data.get('answer', '')
            )
            question.save()
        return quiz
    
    
    
        

    