from api.views import *
from django.urls import path
from rest_framework import routers

urlpatterns = [
    path('projects/', ProjectListAPIView.as_view()),
    path('projects/<int:pk>/', ProjectDetailAPIView.as_view()),
    path('tasks/', TaskAPIView.as_view()),
    path('tasks/<int:pk>/', TaskDetailAPIView.as_view())
]

router = routers.DefaultRouter()
router.register('projects/members', ProjectMemberViewSet, base_name='core')
router.register('tasks/comments', TaskCommentViewSet, base_name='core')
router.register('tasks/documents', TaskDocumentViewSet, base_name='core')
router.register('projects/blocks', BlockViewSet, base_name='core')

urlpatterns += router.urls
