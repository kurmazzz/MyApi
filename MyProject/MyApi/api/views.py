from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from rest_framework import viewsets
from .serializer import ProjectsSerializer, EventsSerializer
from MyApi.models import Project, Event


@api_view()
@permission_classes([AllowAny])
def firstFunction(request):
    print(request.query_params)
    return Response({'message': request.query_params['id']})


@permission_classes([IsAuthenticated])
class ProjectsViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectsSerializer

    # def get_queryset(self):
    #     projects = Project.objects.all()
    #     return projects

    def list(self, request):
        if request.user.is_staff:
            projects = Project.objects.all()
            serializer = ProjectsSerializer(projects, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': "You don`t have permission"})

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        if int(request.user.id) == int(params['pk']) or request.user.is_staff:
            projects = Project.objects.filter(user=params['pk'])
            serializer = ProjectsSerializer(projects, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': "You don`t have permission"})

    def create(self, request, *args, **kwargs):
        project_data = request.data

        new_project = Project.objects.create(name=project_data['name'],
                                             git_url=project_data['git_url'],
                                             user=request.user)
        new_project.save()

        serializer = ProjectsSerializer(new_project)
        return Response(serializer.data)


@permission_classes([IsAuthenticated])
class EventsViewSet(viewsets.ModelViewSet):
    serializer_class = EventsSerializer

    def list(self, request):
        if request.user.is_staff:
            events = Event.objects.all()
            serializer = EventsSerializer(events, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': "You don`t have permission"})

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        if int(request.user.id) == int(params['pk']) or request.user.is_staff:
            events = Event.objects.filter(user=params['pk'])
            serializer = EventsSerializer(events, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': "You don`t have permission"})

    def create(self, request, *args, **kwargs):
        project_data = request.data

        new_events = Event.objects.create(name=project_data['name'],
                                          city=project_data['city'],
                                          user=request.user)
        new_events.save()

        serializer = EventsSerializer(new_events)
        return Response(serializer.data)
