from django.urls import path
from . import views

app_name = "courses"

urlpatterns = [
    path('courses/', views.MyCourseList.as_view(), name='mycourses'),

]