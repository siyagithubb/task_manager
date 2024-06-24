# Generated by Django 5.0.4 on 2024-06-24 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Enter the title of the task', max_length=200)),
                ('description', models.TextField(help_text='Enter a detailed description of the task')),
                ('completed', models.BooleanField(default=False, help_text='Check if the task is completed')),
            ],
        ),
    ]
