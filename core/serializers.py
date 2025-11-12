from rest_framework import serializers
from .models import Xodim


class XodimSerializer(serializers.Serializer):
    full_name = serializers.CharField()
    position = serializers.CharField()
    age = serializers.IntegerField()
    salary = serializers.IntegerField()
    
    def validate_age(self,age):
        if age<18:
            raise serializers.ValidationError("Yoshingiz yetmadi ")
        return age
    
    def is_seniour(self,exp):
        return exp.age >40
            
            
    
    