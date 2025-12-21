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

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password", "password2"]
        extra_kwargs = {
            "email": {"required": True}
        }

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({
                "password": "Passwords do not match!"
            })
        return attrs

    def create(self, validated_data):
        validated_data.pop("password2")
        user = User.objects.create_user(
            username = validated_data["username"],
            email = validated_data["email"],
            password = validated_data["password"]
        )
        return user