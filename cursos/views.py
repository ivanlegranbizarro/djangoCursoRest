from rest_framework import generics

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Course, Evaluation
from .serializers import CourseSerializer, EvaluationSerializer
from .permissions import SuperUserOrReadOnly

from django.shortcuts import get_object_or_404
"""
API V1
"""

# Create your views here.


class CourseAPIView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class EvaluationAPIView(generics.ListCreateAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return Evaluation.objects.filter(
                course_id=self.kwargs.get('curso_pk'))
        return Evaluation.objects.all()


class EvaluationDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(Evaluation,
                                     pk=self.kwargs.get('evaluacion_pk'),
                                     course_id=self.kwargs.get('curso_pk'))
        return get_object_or_404(Evaluation,
                                 pk=self.kwargs.get('evaluacion_pk'))


"""
API V2
"""


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [SuperUserOrReadOnly]

    @action(detail=True, methods=['get'])
    def evaluations(self, request, pk=None):
        course = self.get_object()
        evaluations = Evaluation.objects.filter(course=course)
        serializer = EvaluationSerializer(evaluations, many=True)

        return Response(serializer.data)


class EvaluationViewSet(viewsets.ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer
