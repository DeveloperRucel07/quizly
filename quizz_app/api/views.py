from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from auth_app.api.authentication import CookieJWTAuthentication
from quizz_app.api.serializers import QuizAIGenerateCreateSerializer, QuizSerializer, QuizDetailSerializer
from quizz_app.models import Quiz
from quizz_app.api.permissions import IsOwner


class QuizGenerateAPIView(APIView):
    ''' View to generate a quiz using AI based on a YouTube video URL.
    '''
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = QuizAIGenerateCreateSerializer(
            data=request.data,
            context={'request': request}
        )

        serializer.is_valid(raise_exception=True)
        quiz = serializer.save()

        return Response(QuizSerializer(quiz).data, status=status.HTTP_201_CREATED)

class QuizListView(generics.ListAPIView):
    '''
    View to list and create quizzes for the authenticated user.
    '''
    authentication_classes = [CookieJWTAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = QuizSerializer

    def get_queryset(self):
        '''
        returns only the quizzes of the currently logged-in user.
        '''
        return Quiz.objects.filter(owner=self.request.user)




class QuizRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    '''
    View to retrieve, update or delete a quiz.
    '''
    authentication_classes = [CookieJWTAuthentication]
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer
    permission_classes = [IsAuthenticated, IsOwner]