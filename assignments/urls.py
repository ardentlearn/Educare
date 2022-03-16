from django.urls import path
from . import views

app_name = "assignments"

urlpatterns = [
    path("", views.CourseListView.as_view(), name="course-list"),
    path("course/<int:pk>/", views.CourseQuizzesView.as_view(), name="course-quizzes"),
    path("results/", views.ResultsView.as_view(), name="results"),
    path("delete_quiz/<int:course_id>", views.quiz_delete, name="delete-quiz"),
    path(
        "question_add/<int:pk>", views.QuestionsAddView.as_view(), name="question-add"
    ),
    path(
        "course/create_quiz/<int:course_id>",
        views.CreateQuizView.as_view(),
        name="create-quiz",
    ),
    path(
        "attempt/<int:course_id>/<int:pk>/",
        views.AttemptQuizView.as_view(),
        name="attempt-quiz",
    ),
    path(
        "question_update/<int:course_id>/<int:quiz_id>/<int:pk>/",
        views.QuestionUpdateView.as_view(),
        name="question-update",
    ),
    path(
        "question_delete/<int:course_id>/<int:quiz_id>/<int:pk>/",
        views.QuestionDeleteView.as_view(),
        name="question-delete",
    ),
]
