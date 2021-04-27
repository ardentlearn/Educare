from django.contrib import admin
from .models import Quiz, Quiz_Questions, Results, Questions

# Register your models here.


@admin.register(Quiz_Questions)
class Quiz_Questions(admin.ModelAdmin):
    list_display = (
        "quiz_id",
        "question_id",
    )


@admin.register(Quiz)
class Quiz(admin.ModelAdmin):
    list_display = (
        "quiz_id",
        "course_id",
        "quiz_name",
    )


@admin.register(Results)
class Results(admin.ModelAdmin):
    list_display = (
        "results_id",
        "user",
        "quiz_id",
        "course_id",
        "score",
        "date",
    )


@admin.register(Questions)
class Questions(admin.ModelAdmin):
    list_display = (
        "question_description",
        "choice_1",
        "choice_2",
        "choice_3",
        "choice_4",
        "correct_choice",
    )
