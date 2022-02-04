from django.urls import path

from rest_framework.routers import SimpleRouter

from . import views

router = SimpleRouter()
router.register('courses', views.CourseViewSet)
router.register('evaluations', views.EvaluationViewSet)

urlpatterns = [
    # path('cursos/', views.CourseAPIView.as_view(), name='cursos'),
    # path('evaluaciones/', views.EvaluationAPIView.as_view(), name='evaluaciones')
    path('cursos/', views.CourseAPIView.as_view(), name='cursos'),
    path('curso/<int:pk>/',
         views.CourseDetailAPIView.as_view(),
         name='curso_detail'),
    path('cursos/<int:curso_pk>/evaluaciones/',
         views.EvaluationAPIView.as_view(),
         name='curso_evaluaciones'),
    path('cursos/<int:curso_pk>/evaluaciones/<int:evaluacion_pk>/',
         views.EvaluationDetailAPIView.as_view(),
         name='evaluacion_detail'),
    path('evaluaciones/',
         views.EvaluationAPIView.as_view(),
         name='evaluaciones'),
    path('evaluaciones/<int:evaluacion_pk>/',
         views.EvaluationDetailAPIView.as_view(),
         name='evaluacion_detail'),
]
