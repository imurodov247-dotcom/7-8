from rest_framework import serializers
from .models import Xodim,Student


class XodimSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Xodim
        fields = "__all__"
        
    def get_is_senior(self, obj):
        return obj.age >= 40

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("Age must be at least 18.")
        return value
        
        
        
class StduentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"


        
    def get_grade(self, obj):
        s = obj.score
        if s is None:
            return None
        if 90 <= s <= 100:
            return 'A'
        if 80 <= s <= 89:
            return 'B'
        if 70 <= s <= 79:
            return 'C'
        if 60 <= s <= 69:
            return 'D'
        return 'F'

    def validate_score(self, value):
        if not (0 <= value <= 100):
            raise serializers.ValidationError("Score must be between 0 and 100.")
        return value
            
            
    
    