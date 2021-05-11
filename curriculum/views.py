from django.shortcuts import render
from django.views.generic import (TemplateView, DetailView, ListView, FormView)
from curriculum.models import Branch, Subject, Lesson

# Create your views here.
class BranchListView(ListView):
    context_object_name = 'branch_names'
    model = Branch
    template_name = 'curriculum/Branch_List_View.html'

class SubjectListView(DetailView):
    context_object_name = 'branch_names'
    model = Branch
    template_name = 'curriculum/Subject_List_View.html'

class LessonListView(DetailView):
    context_object_name = 'subjects'
    model = Subject
    template_name = 'curriculum/lesson_list_view.html'

class LessonDetailView(DetailView):
    context_object_name = 'lessons'
    model = Lesson
    template_name = 'curriculum/lesson_detail_view.html'
