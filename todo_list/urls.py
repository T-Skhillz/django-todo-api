from django.urls import path
from todo_list import views

urlpatterns = [
    path("", views.api_root, name = "api-root"),
    #path("login/", views.MyTokenObtainPairView.as_view(), name = "token_obtain_pair"),
    path("users/", views.UserList.as_view(),  name = "user-list"),
    path("tasks/", views.TaskList.as_view(), name = "task-list"),
    path("tasks/<int:pk>/", views.TaskDetail.as_view(), name = "task-detail"),
]