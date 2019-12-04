from datetime import datetime

from django.db import models

from api.constants import TASK_TYPES, TASK_NEW
from user.models import MainUser


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300, blank=True, default='')
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='created_projects')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'project'
        ordering = ('created_at', )

    def __str__(self):
        return self.name + '\n' + self.description

    def get_short_description(self):
        return self.description[: 10] + '...'


class ProjectMember(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='assigned_projects')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')
    joined_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'project_member'
        ordering = ('joined_at', )

    def __str__(self):
        return self.project.name + ' member ' + self.user.profile.full_name


class NewTasksBlockManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(type=TASK_NEW)

    def new_tasks(self):
        return self.filter(type=TASK_NEW)

    def filter_by_type(self, status):
        return self.filter(type=type)


class Block(models.Model):
    name = models.CharField(max_length=20)
    type = models.PositiveSmallIntegerField(choices=TASK_TYPES, default=TASK_NEW)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='blocks')

    objects = models.Manager()
    new_tasks_block = NewTasksBlockManager()

    class Meta:
        db_table = 'block'
        ordering = ('type', )

    def __str__(self):
        return self.name + ' ' + self.project.name


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300, blank=True)
    order = models.IntegerField()
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='created_tasks')
    executor = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='assigned_tasks')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'task'
        # unique_together = ('block', 'order', )
        ordering = ('block', 'order', )

    def __str__(self):
        return self.name + '\n' + self.description

    @classmethod
    def get_recent_projects(cls):
        today = datetime.now()
        return cls.objects.filter(created_at__day=today.day,
                                  created_at__month=today.month,
                                  created_at__year=today.year)


class TaskDocument(models.Model):
    document = models.FileField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='documents')
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='uploaded_documents')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'task_document'
        ordering = ('created_at', )

    @staticmethod
    def get_doc_len(doc):
        return len(doc.document)


class TaskComment(models.Model):
    body = models.TextField(max_length=200)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='tasks_comments')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'task_comment'
        ordering = ('created_at', )

    def __str__(self):
        return self.creator.username + ': ' + self.body
