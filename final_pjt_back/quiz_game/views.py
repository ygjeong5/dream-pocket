from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from .models import Quiz
from .serializers import QuizSerializer
import random

@api_view(['GET'])
@authentication_classes([])
@permission_classes([AllowAny])
def random_quiz(request, count):
    try:
        level = request.GET.get('level', 'beginner')  # 기본값은 초급
        total_quizzes = Quiz.objects.filter(level=level)
        
        if not total_quizzes.exists():
            return Response(
                {"error": f"{level} 레벨의 퀴즈가 없습니다."}, 
                status=status.HTTP_404_NOT_FOUND
            )
        
        available_count = min(total_quizzes.count(), count)
        random_quizzes = random.sample(list(total_quizzes), available_count)
        serializer = QuizSerializer(random_quizzes, many=True)
        return Response(serializer.data)
        
    except Exception as e:
        print(f"Error in random_quiz view: {str(e)}")
        return Response(
            {"error": f"서버 오류가 발생했습니다: {str(e)}"}, 
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
