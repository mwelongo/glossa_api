from django.urls import path
from . import views

urlpatterns = [
    path('api/lessons', views.LessonList.as_view(), name='lesson_list'),
    path('api/lessons/<int:pk>', views.LessonDetail.as_view(), name='lessons_detail')
]
