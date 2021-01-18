from django.conf.urls import url
from django.urls import include
from .views import firstFunction
from rest_framework.routers import DefaultRouter
from .views import ProjectsViewSet, EventsViewSet

router = DefaultRouter()
router.register('projects', ProjectsViewSet, basename='projects')
router.register('events', EventsViewSet, basename='events')

urlpatterns = [
    url('first', firstFunction),
    url('', include(router.urls))
]
