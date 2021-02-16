# Generated by Django 3.1.5 on 2021-02-16 17:01

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('color', models.CharField(max_length=7, validators=[django.core.validators.RegexValidator(message='Color must have a hex value', regex='^#([a-fA-F0-9]{6}|[a-fA-F0-9]{3})$')])),
                ('repo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='repository.repository', verbose_name='repo')),
            ],
        ),
    ]
