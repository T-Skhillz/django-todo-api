from rest_framework.decorators import api_view
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import generics
from django.contrib.auth.models import User
from todo_list import serializers
from django.shortcuts import get_object_or_404
from .models import Task
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


#function for root url of users and tasks
@api_view(["GET"])
def api_root(request):
    return Response(
        {
            "user" : reverse("user-list", request=request, format=None),
            "tasks": reverse("task-list", request=request, format=None),
        }
    )

#view for user registration
class UserRegistration(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserRegistrationSerializer
    permission_classes = []

#view for list of users
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = (IsAuthenticated,)

#view for list of tasks
class TaskList(APIView):
    def get(self, request):
        tasks = Task.objects.filter(user=request.user)
        serializer = serializers.TaskSerializer(tasks, many=True, context={"request": request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = serializers.TaskSerializer(data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = (IsAuthenticated,)

#view for detail of one task object
class TaskDetail(APIView):
    def get_object(self, pk):
        return get_object_or_404(Task, user=self.request.user, pk=pk)

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = serializers.TaskSerializer(task, context={"request": request})
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = serializers.TaskSerializer(task, data=request.data, context={"request": request})
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    permission_classes = (IsAuthenticated,)