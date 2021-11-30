from rest_framework import serializers
from .models import Lesson

class LessonSerializer(serializers.ModelSerializer): # serializers.ModelSerializer will instruct django to convert sql to JSON

class Meta:
        model = Lesson
        fields = ('id', 'module_title', 'module_instructor', 'module_description', 'module_objectives', 'lesson_num', 'lesson_title', 'lesson_subtitle', 'lesson_notes', 'lesson_image')
        # fields tell django which fields from the model to include
