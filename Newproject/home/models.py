from django.db import models

# Create your models here.
class student(models.Model):
      Name = models.CharField(max_length=50)
      Cls = models.IntegerField()
      Roll = models.IntegerField()
      class Meta:
            db_table = 'student'
      

