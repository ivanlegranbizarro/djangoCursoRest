from rest_framework import serializers
from .models import Course, Evaluation
from django.db.models import Avg


class EvaluationSerializer(serializers.ModelSerializer):
    course = serializers.StringRelatedField()

    class Meta:
        model = Evaluation
        extra_kwargs = {'email': {'write_only': True}}
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    # evaluations = EvaluationSerializer(many=True, read_only=True)
    evaluations = serializers.HyperlinkedRelatedField(
        view_name='evaluation-detail', read_only=True, many=True)
    media_evaluations = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    # Haríamos esta validación si no fuera porque ya está en el modelo

    # def validate_evaluation(self, valor):
    #     if valor in range(1, 5):
    #         return valor
    #     raise serializers.ValidationError(
    #         'La evaluación debe estar entre 1 y 5')

    def get_media_evaluations(self, obj):
        media = obj.evaluations.aggregate(media=Avg('score'))['media']
        if media:
            return round(media, 2)
        return 0
