from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Quiz, Questions, Quiz_Questions, Results
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib import messages
from .forms import QuestionUpdateForm, CreateQuizForm
from curriculum.models import Branch
import json


class SuperUserRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class CourseListView(ListView):
    template_name = "assignments/course_list.html"
    model = Branch
    context_object_name = "courses"


class CourseQuizzesView(LoginRequiredMixin, ListView):
    template_name = "assignments/course_quizzes.html"
    model = Quiz
    context_object_name = "quizzes"

    def get_queryset(self):
        queryset = Quiz.objects.filter(course_id=self.kwargs.get("pk"))
        return queryset

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["course_name"] = Branch.objects.get(pk=self.kwargs.get("pk")).name
        data["course_id"] = self.kwargs.get("pk")
        return data


class AttemptQuizView(LoginRequiredMixin, TemplateView):
    template_name = "assignments/attempt_quiz.html"
    context_object_name = "questions"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["questions"] = Quiz_Questions.objects.filter(quiz_id=self.kwargs.get("pk"))
        return data

    def post(self, request, **kwargs):
        try:
            score = 0
            data = json.loads(request.body)
            response_data = {}

            for key, value in data.items():
                if key.isdigit():
                    correct_answer = Questions.objects.get(pk=key).correct_choice
                    response_data[key] = correct_answer
                    if value != "none" and int(value) == correct_answer:
                        score += 1

            response_data["score"] = score

            Results.objects.create(
                quiz_id=Quiz.objects.get(quiz_id=self.kwargs.get("pk")),
                course_id=Branch.objects.get(pk=self.kwargs.get("course_id")),
                score=score,
                user=request.user,
            )

        except Exception as e:
            print(e)

        return JsonResponse(response_data)


class QuestionUpdateView(SuperUserRequiredMixin, LoginRequiredMixin, UpdateView):
    template_name = "assignments/question_update.html"
    form_class = QuestionUpdateForm
    queryset = Questions.objects.all()
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["course_id"] = self.kwargs.get("course_id")
        data["quiz_id"] = self.kwargs.get("quiz_id")
        return data

    def get_success_url(self):
        messages.success(self.request, "Question has been updated")
        return reverse_lazy(
            "assignments:attempt-quiz",
            kwargs={
                "course_id": self.kwargs.get("course_id"),
                "pk": self.kwargs.get("quiz_id"),
            },
        )


class QuestionDeleteView(SuperUserRequiredMixin, LoginRequiredMixin, DeleteView):
    template_name = "assignments/question_delete.html"
    queryset = Questions.objects.all()

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)

    def get_success_url(self):
        messages.success(self.request, "Deleted successfully")
        return reverse_lazy(
            "assignments:attempt-quiz",
            kwargs={
                "course_id": self.kwargs.get("course_id"),
                "pk": self.kwargs.get("quiz_id"),
            },
        )


class QuestionsAddView(SuperUserRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = "assignments/question_add.html"
    form_class = QuestionUpdateForm

    def get_success_url(self):
        try:
            latest_question_id = Questions.objects.latest("question_id")
            Quiz_Questions.objects.create(
                quiz_id=Quiz.objects.get(quiz_id=self.kwargs.get("pk")),
                question_id=latest_question_id,
            )
            messages.success(self.request, "Question has been added")
        except Exception as e:
            messages.error(self.request, "An error occurred")

        return self.request.path


class CreateQuizView(SuperUserRequiredMixin, LoginRequiredMixin, CreateView):
    template_name = "assignments/create_quiz.html"
    form_class = CreateQuizForm

    def form_valid(self, form):
        form.instance.course_id = Branch.objects.get(pk=self.kwargs.get("course_id"))
        return super(CreateQuizView, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "New Quiz has been created")
        return reverse_lazy(
            "assignments:question-add",
            kwargs={"pk": Quiz.objects.latest("quiz_id").quiz_id},
        )


class ResultsView(LoginRequiredMixin, ListView):
    template_name = "assignments/results.html"
    model = Results
    context_object_name = "results"

    def get_queryset(self):
        return Results.objects.filter(user=self.request.user)


def quiz_delete(request, **kwargs):
    try:
        if request.method == "POST":
            Quiz.objects.get(quiz_id= request.POST.get('quiz_id')).delete()
            course_id = kwargs['course_id']
            messages.success(request, "Quiz deleted successfully")
        else:
            return HttpResponse("Invalid")
    except Exception:
        return HttpResponse("An error occurred")

    return HttpResponseRedirect(reverse_lazy("assignments:course-quizzes", kwargs= {"pk" : course_id}))
    
