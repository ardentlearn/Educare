# Generated by Django 3.2.2 on 2021-05-12 19:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courses', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_description', models.TextField(null=True)),
                ('choice_1', models.CharField(max_length=200, null=True)),
                ('choice_2', models.CharField(max_length=200, null=True)),
                ('choice_3', models.CharField(max_length=200, null=True)),
                ('choice_4', models.CharField(max_length=200, null=True)),
                ('correct_choice', models.IntegerField()),
                ('question_image_address', models.ImageField(blank=True, null=True, upload_to='images/')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_id', models.AutoField(primary_key=True, serialize=False)),
                ('quiz_name', models.CharField(max_length=200)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='Results',
            fields=[
                ('results_id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('score', models.IntegerField(blank=True, null=True)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.course')),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.quiz')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz_Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.questions')),
                ('quiz_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='assignments.quiz')),
            ],
        ),
    ]
