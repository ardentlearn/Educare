from django.urls import path
from . import views

app_name='curriculum'
urlpatterns = [
    path('', views.BranchListView.as_view(), name='branch_list'),
    path('<slug:slug>/', views.SubjectListView.as_view(), name='subject_list'),
    path('<str:Branch>/<slug:slug>/', views.LessonListView.as_view(), name='lesson_list'),
    path('<str:Branch>/<str:subject>/<slug:slug>/', views.LessonDetailView.as_view(), name='lesson_detail'),


]