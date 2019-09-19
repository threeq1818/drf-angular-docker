from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer

from rest_framework import generics

# Create your views here.

class TaskList(generics.ListAPIView):
    """
    For GET requests.
    View all tasks.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer