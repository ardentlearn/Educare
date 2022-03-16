# Generated by Django 3.1.7 on 2021-06-13 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_branch_image'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCourseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('added', models.BooleanField(default=False)),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.subject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'UserCourseInfo',
                'verbose_name_plural': 'UserCourseInfos',
            },
        ),
        migrations.AddField(
            model_name='course',
            name='student_course',
            field=models.ManyToManyField(to='courses.UserCourseInfo'),
        ),
    ]