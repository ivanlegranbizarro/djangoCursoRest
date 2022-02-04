from django.contrib import admin
from .models import Course, Evaluation

# Register your models here.


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'url', 'active', 'created_at', 'updated_at')
    search_fields = ('name', 'url')


@admin.register(Evaluation)
class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'name', 'score', 'created_at',
                    'updated_at', 'active')
    search_fields = ('course', 'name')
