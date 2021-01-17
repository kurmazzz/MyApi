from django.conf.urls import url
from django.urls import include
from .views import firstFunction
from rest_framework.routers import DefaultRouter
from .views import ProjectsViewSet

router = DefaultRouter()
router.register('projects', ProjectsViewSet, basename='projects')

urlpatterns = [
    url('first', firstFunction),
    url('', include(router.urls))
]