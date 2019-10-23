from rest_framework import serializers

from api.models import Project, ProjectMember, TaskDocument, Block, Task, TaskComment
from user.serializer import UserSerializer


class ProjectSerializer(serializers.ModelSerializer):
    creator_id = serializers.IntegerField(write_only=True)
    creator_name = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ('id', 'name', 'description', 'creator_name', 'creator_id')

    def get_creator_name(self, obj):
        if obj.creator is not None:
            return obj.creator.username
        return ''


class ProjectMemberSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    project = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ProjectMember
        fields = '__all__'


class BlockSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Block
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)
    executor = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Task
        fields = '__all__'


class TaskDocumentSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(read_only=True)
    creator = UserSerializer(read_only=True)

    class Meta:
        model = TaskDocument
        fields = '__all__'


class TaskCommentSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(read_only=True)
    creator = UserSerializer(read_only=True)

    class Meta:
        model = TaskComment
        fields = '__all__'
