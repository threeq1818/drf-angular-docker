from django.shortcuts import render
from .models import Task
from .serializers import TaskSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class TaskList(APIView):
    """
    For GET requests.
    View all tasks.
    """
    def get(self, request, format=None):
        """
        :param request:
        :param format:
        :return: a list of all tasks.
        """
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)