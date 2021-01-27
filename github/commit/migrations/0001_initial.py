# Generated by Django 3.1.5 on 2021-01-27 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sha', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=200)),
                ('size', models.IntegerField()),
                ('commitedDate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]