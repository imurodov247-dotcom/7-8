from django.db import models

# Create your models here.
class Xodim(models.Model):
    full_name = models.CharField()
    position = models.CharField()
    age = models.IntegerField()
    salary = models.CharField()
    
    
    def __str__(self):
        return self.full_name