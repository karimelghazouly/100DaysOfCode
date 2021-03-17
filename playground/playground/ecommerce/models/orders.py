from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user_id = models.ForeignKey(User, models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)