from django.db import models

class Student(models.Model):
    userid=models.IntegerField()
    name=models.CharField(max_length=80)
    course=models.CharField(max_length=50)
    branch=models.CharField(max_length=80)
    rollno=models.IntegerField()
    batch=models.IntegerField()
    def _str_(self):
        return self.userid


# Create your models here.
