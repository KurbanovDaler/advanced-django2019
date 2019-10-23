from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from api.models import ProjectMember, TaskComment, Block
from api.serializers import ProjectMemberSerializer, TaskCommentSerializer, BlockSerializer, TaskSerializer


class ProjectMemberViewSet(viewsets.ModelViewSet):
    queryset = ProjectMember.objects.all()
    serializer_class = ProjectMemberSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TaskCommentViewSet(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class TaskDocumentViewSet(viewsets.ModelViewSet):
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    @action(methods=['GET'], detail=True)
    def tasks(self, request, pk):
        block = self.get_object()
        serializer = TaskSerializer(block.tasks, many=True)
        return Response(serializer.data)


