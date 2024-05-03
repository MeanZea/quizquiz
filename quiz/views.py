import random

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Quiz
from .serealizer import QuizSerializer


@api_view(['GET'])
def helloAPI(request):
    return Response("hello world!")

@api_view(['GET'])
def randomQuiz(request, id):
    totalQuizs = Quiz.objects.all()
    randomQuizs = random.sample(list(totalQuizs),id)
    sserializer = QuizSerializer(randomQuizs, many=True)
    return Response(sserializer.data)
    