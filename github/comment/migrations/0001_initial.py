# Generated by Django 3.1.5 on 2021-01-29 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=300)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('task', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='task.task')),
            ],
        ),
    ]
