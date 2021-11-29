from django.db import models

# Create your models here.
class Lesson(models.Model):
    module_title = models.CharField(max_length=120)
    module_instructor = models.CharField(max_length=120)
    module_description = models.CharField(max_length=3200)
    module_objectives = models.CharField(max_length=600)
    lesson_num = models.IntegerField()
    lesson_title = models.CharField(max_length=300)
    lesson_subtitle = models.CharField(max_length=300)
    lesson_notes = models.CharField(max_length=3200)
    lesson_image = models.CharField(max_length=200)
