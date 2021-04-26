from django.urls import path
from . import views

app_name = "assignments"

urlpatterns = [
    path("", views.CourseListView.as_view(), name="course-list"),
    path("course/<int:pk>/", views.CourseQuizzesView.as_view(), name="course-quizzes"),
    path(
        "question_add/<int:pk>", views.QuestionsAddView.as_view(), name="question-add"
    ),
    # path(
    #     "course/create_quiz/<int:course_id>",
    #     views.CreateQuizView.as_view(),
    #     name="create-quiz",
    # ),
    path("results/", views.ResultsView.as_view(), name="results"),
    path(
        "attempt/<str:couse_name>/<int:course_id>/<int:pk>/",
        views.AttemptQuizView.as_view(),
        name="attempt-quiz",
    ),
    path(
        "question_update/<int:pk>",
        views.QuestionUpdateView.as_view(),
        name="question-update",
    ),
    path(
        "question_delete/<int:pk>",
        views.QuestionDeleteView.as_view(),
        name="question-delete",
    ),
]
