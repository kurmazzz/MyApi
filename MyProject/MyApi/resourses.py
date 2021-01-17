from import_export import resources
from MyApi.models import Project

class ProjectResourse(resources.ModelResourse):
    class Meta:
        model = Project
