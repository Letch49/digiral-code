from django.db import models

from users.models import User


class Task(models.Model):
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.TextField()
    description = models.TextField()
    time_limit = models.IntegerField()
    memory_limit = models.IntegerField()
    tests = models.JSONField()


class Solution(models.Model):
    STATUS_NEW = 'new'
    STATUS_PROCESSING = 'processing'
    STATUS_RIGHT = 'right'
    STATUS_WRONG = 'wrong'

    STATUSES = [
        STATUS_NEW, STATUS_PROCESSING, STATUS_RIGHT, STATUS_WRONG
    ]

    STATUSES_CHOICES = {o: o for o in STATUSES}

    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='*')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='solutions')
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUSES_CHOICES, max_length=25, default=STATUS_NEW)
    score = models.IntegerField(default=0)
