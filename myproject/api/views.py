from rest_framework import viewsets
from .models import Task
from .serializers import TaskSerializer

# ViewSet для модели Task

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer



