from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import LessonSerializer
from .models import Lesson

class LessonList(generics.ListCreateAPIView):
    queryset = Lesson.objects.all().order_by('id')
    # Django will retrieve all objects from the DB and order them by id ascending
    serializer_class = LessonSerializer

class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all().order_by('id')
    serializer_class = LessonSerializer
