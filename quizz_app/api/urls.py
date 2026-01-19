from django.urls import path
from quizz_app.api.views import QuizGenerateAPIView, QuizListView, QuizRetrieveUpdateDeleteView

urlpatterns = [
   path('createQuiz/', QuizGenerateAPIView.as_view(), name='quiz-create'),
   path('quizzes/', QuizListView.as_view(), name='quiz-list'),
   path('quizzes/<int:pk>/', QuizRetrieveUpdateDeleteView.as_view(), name='quiz-detail'),
]