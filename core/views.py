from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import XodimSerializer 
from rest_framework.response import Response
from .serializers import XodimSerializer,StduentSerializer
from .models import Xodim,Student
from rest_framework.viewsets import ModelViewSet

class XodimViewSet(ModelViewSet):
    queryset = Xodim.objects.all()
    serializer_class = XodimSerializer
    
    def get_queryset(self):
        qs = super().get_queryset()
        if self.action == 'list':
            queryset = qs.filter(salary__gte=1000)
        return queryset
    
    
class StudentModelViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StduentSerializer
    
    
    
