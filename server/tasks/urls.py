from django.urls import path

from tasks.api import TeacherTaskListCreateAPI, TeacherTaskRetrieveUpdateDeleteAPI, TaskListAPI, SolutionListCreateAPI, \
    TeacherSolutionListAPI, SolutionRetrieveDeleteAPI, TaskRetrieveAPI

urlpatterns = [
    path('teacher/tasks', TeacherTaskListCreateAPI.as_view()),
    path('teacher/tasks/<int:id>', TeacherTaskRetrieveUpdateDeleteAPI.as_view()),
    path('teacher/solutions', TeacherSolutionListAPI.as_view()),

    path('tasks', TaskListAPI.as_view()),
    path('tasks/<int:id>', TaskRetrieveAPI.as_view()),
    path('solutions', SolutionListCreateAPI.as_view()),
    path('solutions/<int:id>', SolutionRetrieveDeleteAPI.as_view()),
]
