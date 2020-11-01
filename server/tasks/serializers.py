from django.db import transaction
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from tasks.models import Task, Solution
from users.serializers import UserSerializer


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    is_active = serializers.BooleanField(required=False)
    created = serializers.DateTimeField(required=False)
    creator = UserSerializer(required=False)
    title = serializers.CharField()
    description = serializers.CharField()
    time_limit = serializers.IntegerField()
    memory_limit = serializers.IntegerField()
    tests = serializers.JSONField()

    @transaction.atomic(savepoint=False)
    def create(self, validated_data):
        return Task.objects.create(
            creator=validated_data.get('creator'),
            title=validated_data.get('title'),
            description=validated_data.get('description'),
            time_limit=validated_data.get('time_limit'),
            memory_limit=validated_data.get('memory_limit'),
            tests=validated_data.get('tests'),
        )

    @transaction.atomic(savepoint=False)
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title')
        instance.description = validated_data.get('description')
        instance.time_limit = validated_data.get('time_limit')
        instance.memory_limit = validated_data.get('memory_limit')
        instance.tests = validated_data.get('tests')
        instance.save()
        return instance

    class Meta:
        model = Task


class SolutionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    owner = UserSerializer(required=False)
    task = TaskSerializer(required=False)
    task_id = serializers.SerializerMethodField()
    text = serializers.CharField()
    language = serializers.CharField()
    created = serializers.DateTimeField(required=False)
    status = serializers.CharField(required=False)
    score = serializers.IntegerField(required=False)

    def get_task_id(self, instance):
        return instance.task.id

    @transaction.atomic(savepoint=False)
    def create(self, validated_data, user):
        return Solution.objects.create(
            owner=validated_data.get('owner'),
            task=get_object_or_404(Task, id=validated_data.get('task_id')),
            text=validated_data.get('text'),
            language=validated_data.get('language'),
        )

    class Meta:
        model = Solution
