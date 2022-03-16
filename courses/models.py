from curriculum.models import Subject
from django.db.models.signals import post_save
from django.db import models
from accounts.models import User
from curriculum.models import Subject
from django.dispatch import receiver



class UserCourseInfo(models.Model):
    
    user = models.ForeignKey(User , null = False , on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject , null = False , on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    added = models.BooleanField(default=False)

    
    # this method called for admin panel
    class Meta:
        verbose_name = 'UserCourseInfo'
        verbose_name_plural = 'UserCourseInfos'

    def __str__(self):
        return f'{self.user} - {self.subject.name}'

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=200)
    student_course = models.ManyToManyField(UserCourseInfo)
    

    def __str__(self):
        return str(self.course_name)


    
    

