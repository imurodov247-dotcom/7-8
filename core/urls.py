from django.urls import path,include
from .views import XodimViewSet,StudentModelViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('api_x',XodimViewSet)
router.register('api_t',StudentModelViewSet)

urlpatterns = [

    path("",include(router.urls)),
    path("",include(router.urls)),
]