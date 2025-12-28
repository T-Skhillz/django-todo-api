from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = {
        "work" : "Work", 
        "school" : "School", 
        "business" : "Business", 
        "personal" : "Personal", 
        "recreational" : "Recreational",
    }

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks")
    title = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    category = models.CharField(
        choices=CATEGORY_CHOICES,
        default="work",
        max_length=100
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        ordering = ("-created_on",)

