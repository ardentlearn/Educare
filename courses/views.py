from django.http.response import HttpResponse, JsonResponse
from curriculum.models import Subject
from django.shortcuts import render
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.views.generic.list import ListView
from .models import Course, UserCourseInfo,User
# Create your views here.


class MyCourseList(ListView):
    context_object_name = 'mycourses'
    model = UserCourseInfo
    template_name = 'courses/MyCourses.html'

    def get_queryset(self):
        return UserCourseInfo.objects.filter(user = self.request.user)

    


