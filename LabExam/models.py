from django.db import models

class LabExam(models.Model):
    auto_increment_id=models.AutoFIeld(primary_key=True)
    exam_date=models.DateField()
    exam_name=models.CharField(max_length=50)
    exam_description=models.TextField(max_length=200)
    total_marks=models.FloatField()
    pass_marks=models.FloatField()
    exam_status=models.BooleanField()
