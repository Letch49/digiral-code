from django.db import transaction
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404, ListAPIView, \
    RetrieveDestroyAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import Task, Solution
from tasks.serializers import TaskSerializer, SolutionSerializer
from users.api import IsTeacher


class TeacherTaskListCreateAPI(ListCreateAPIView):
    permission_classes = [IsTeacher]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(creator=self.request.user)


class TeacherTaskRetrieveUpdateDeleteAPI(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsTeacher]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'id'

    def filter_queryset(self, queryset):
        return queryset.filter(owner=self.request.user)

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()


class TeacherSolutionListAPI(ListAPIView):
    permission_classes = [IsTeacher]
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(task__creator=self.request.user)


class TaskListAPI(ListAPIView):
    permission_classes = [AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(is_active=True)


class TaskRetrieveAPI(RetrieveAPIView):
    permission_classes = [AllowAny]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'id'

    def filter_queryset(self, queryset):
        return queryset.filter(is_active=True)


class SolutionListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer

    def filter_queryset(self, queryset):
        return queryset.filter(owner=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(owner=self.request.user)


class SolutionRetrieveDeleteAPI(RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Solution.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'id'
    lookup_field = 'id'

    def filter_queryset(self, queryset):
        return queryset.filter()

    def perform_destroy(self, instance):
        if instance.owner.id != self.request.user.id:
            raise PermissionDenied()
        instance.delete()
