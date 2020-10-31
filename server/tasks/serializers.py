from django.db import transaction
from rest_framework import serializers

from tasks.models import Task
from users.serializers import UserSerializer


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    is_active = serializers.BooleanField(required=False)
    created = serializers.DateTimeField(required=False)
    creator = UserSerializer()
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
