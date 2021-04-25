from django.contrib import admin
from .models import  Quiz, Quiz_Questions, Results, Questions
# Register your models here.

admin.site.register(Quiz)
admin.site.register(Quiz_Questions)
admin.site.register(Results)

@admin.register(Questions)
class Questions(admin.ModelAdmin):
    list_display = (
        "question_description",
        "choice_1",
        "choice_2",
        "choice_3",
        "choice_4",
        "correct_choice"
    )
