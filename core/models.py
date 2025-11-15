from django.db import models

# Create your models here.
class Xodim(models.Model):
    full_name = models.CharField()
    position = models.CharField()
    age = models.IntegerField()
    salary = models.CharField()
    
    
    def __str__(self):
        return self.full_name
    
    
class Student(models.Model):
    name = models.CharField()
    subject = models.CharField()
    score = models.IntegerField()
    
    
    def __str__(self):
        return f"{self.name} {self.subject} {self.score}"
    
    
