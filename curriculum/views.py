from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import (
    TemplateView, DetailView, ListView, FormView, CreateView, UpdateView, DeleteView)
from curriculum.models import Branch, Subject, Lesson
from .forms import LessonForm

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

    template_name = 'curriculum/lesson_detail_view.html'


class LessonCreateView(CreateView):
    # fields = ('lesson_id','name','position','image','video','ppt','Notes')
    form_class = LessonForm
    context_object_name = 'subject'
    model = Subject
    template_name = 'curriculum/lesson_create.html'

    def get_success_url(self):
        self.object = self.get_object()
        Branch = self.object.Branch
        return reverse_lazy('curriculum:lesson_list', kwargs={'Branch': Branch.slug,
                                                              'slug': self.object.slug})

    def form_valid(self, form, *args, **kwargs):
        self.object = self.get_object()
        fm = form.save(commit=False)
        fm.created_by = self.request.user
        fm.Branch = self.object.Branch
        fm.subject = self.object
        fm.save()
        return HttpResponseRedirect(self.get_success_url())


class LessonUpdateView(UpdateView):
    fields = ('name', 'position', 'video', 'ppt', 'Notes')
    model = Lesson
    template_name = 'curriculum/lesson_update.html'
    context_object_name = 'lessons'


class LessonDeleteView(DeleteView):
    model = Lesson
    template_name = 'curriculum/lesson_delete.html'
    context_object_name = 'lessons'


    def get_success_url(self):
        print(self.object)
        Branch = self.object.Branch
        subject = self.object.subject
        return reverse_lazy('curriculum:lesson_list',kwargs={'Branch':Branch.slug,'slug':subject.slug})
