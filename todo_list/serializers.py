from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Task
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TaskSerializer(serializers.ModelSerializer):
    #user = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.ReadOnlyField(source="user.username")
    task_url = serializers.HyperlinkedIdentityField(read_only=True, view_name="task-detail")

    class Meta:
        model = Task
        fields = [
            "id",
            "user",
            "title",
            "completed",
            "category",
            "created_on",
            "task_url",
      ]
        read_only_fields = ["created_on"]

class UserSerializer(serializers.ModelSerializer):
    queryset = User.objects.all()
    tasks = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="task-detail")

    class Meta:
        model = User
        fields = ["id", "username", "tasks"]
