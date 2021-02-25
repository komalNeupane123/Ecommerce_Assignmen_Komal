from django.db import models

# Create your models here.
class LabExam(models.Model):
    exam_date = models.DateTimeField()
    exam_name = models.CharField(max_length=20)
    exam_description = models.CharField(max_length=500)
    total_marks = models.FloatField()
    pass_marks = models.FloatField()
    exam_status = models.BooleanField()