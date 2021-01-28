# Generated by Django 3.1.5 on 2021-01-28 19:09

from django.db import migrations, models
import task.models


class Migration(migrations.Migration):

    dependencies = [
        ('label', '0001_initial'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='closingDate',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='label',
            field=models.ManyToManyField(to='label.Label'),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskPriorty',
            field=models.CharField(choices=[(task.models.TaskPriorty['LOW'], 'LOW'), (task.models.TaskPriorty['MEDUIM'], 'MEDUIM'), (task.models.TaskPriorty['HIGH'], 'HIGH')], default='LOW', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskState',
            field=models.CharField(choices=[(task.models.TaskState['OPENED'], 'OPENED'), (task.models.TaskState['CLOSED'], 'CLOSED')], default='OPENED', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskStatus',
            field=models.CharField(choices=[(task.models.TaskStatus['TO_DO'], 'TO_DO'), (task.models.TaskStatus['IN_PROGRESS'], 'IN_PROGRESS'), (task.models.TaskStatus['TEST'], 'TEST'), (task.models.TaskStatus['DONE'], 'DONE')], default='TO_DO', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='taskType',
            field=models.CharField(choices=[(task.models.TaskType['BUG_FIX'], 'BUG_FIX'), (task.models.TaskType['FEATURE'], 'FEATURE')], default='FEATURE', max_length=50),
        ),
    ]