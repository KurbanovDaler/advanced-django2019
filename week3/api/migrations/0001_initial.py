# Generated by Django 2.2.5 on 2019-10-23 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'New'), (1, 'ToDo'), (2, 'InProgress'), (3, 'Done')], default=0)),
            ],
            options={
                'ordering': ('type',),
                'db_table': 'block',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, default='', max_length=300)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created_at',),
                'db_table': 'project',
            },
        ),
        migrations.CreateModel(
            name='ProjectMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('joined_at',),
                'db_table': 'project_member',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=300)),
                ('order', models.IntegerField()),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('block', 'order'),
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='TaskComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=200)),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created_at',),
                'db_table': 'task_comment',
            },
        ),
        migrations.CreateModel(
            name='TaskDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document', models.FileField(upload_to='')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
            options={
                'ordering': ('created_at',),
                'db_table': 'task_document',
            },
        ),
    ]
