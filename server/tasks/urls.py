from django.urls import path

from tasks.api import AppealListCreateAPI, AppealRetrieveUpdateCancelAPI, AppealSaveDocumentAPI, AppealSendAPI

urlpatterns = [
    path('', AppealListCreateAPI.as_view(), name='appeals'),
    path('<int:id>', AppealRetrieveUpdateCancelAPI.as_view(), name='appeal'),
    path('<int:id>/file', AppealSaveDocumentAPI.as_view(), name='appeal_file'),
    path('<int:id>/send', AppealSendAPI.as_view(), name='appeal_send'),
]
