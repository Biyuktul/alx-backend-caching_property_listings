from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default="No description provided")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
