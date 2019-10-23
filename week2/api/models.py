from django.db import models

from user.models import MainUser


class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    creator = models.ForeignKey(MainUser, on_delete=models.DO_NOTHING, related_name='created_projects')


class ProjectMember(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='assigned_projects')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='members')


class Block(models.Model):
    NEW = 0
    TO_DO = 1
    IN_PROGRESS = 2
    DONE = 3
    TYPES = (
        (NEW, 'New'),
        (TO_DO, 'ToDo'),
        (IN_PROGRESS, 'InProgress'),
        (DONE, 'Done'),
    )

    name = models.CharField(max_length=20)
    type = models.IntegerField(choices=TYPES, default=NEW)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='blocks')


class Task(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    order = models.IntegerField(unique=True)
    creator = models.ForeignKey(MainUser, on_delete=models.DO_NOTHING, related_name='created_tasks')
    executor = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='assigned_tasks')
    block = models.ForeignKey(Block, on_delete=models.CASCADE, related_name='tasks')


class TaskDocument(models.Model):
    document = models.FileField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='documents')
    creator = models.ForeignKey(MainUser, on_delete=models.DO_NOTHING, related_name='uploaded_documents')


class TaskComment(models.Model):
    body = models.TextField(max_length=200)
    creator = models.ForeignKey(MainUser, on_delete=models.CASCADE, related_name='tasks_comments')
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')