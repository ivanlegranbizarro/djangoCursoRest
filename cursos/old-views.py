from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer


# Create your views here.


class CourseAPIView(APIView):
    """
    API con el listado de cursos
    """

    @staticmethod
    def get(request):
        cursos = Course.objects.all()
        serializer = CourseSerializer(cursos, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EvaluationAPIView(APIView):
    """
    API con el listado de evaluaciones
    """

    @staticmethod
    def get(request):
        evaluations = Evaluation.objects.all()
        serializer = EvaluationSerializer(evaluations, many=True)
        return Response(serializer.data)

    @staticmethod
    def post(request):
        serializer = EvaluationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
