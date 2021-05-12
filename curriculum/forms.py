from django import forms
from django.forms import fields
from .models import Lesson

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ('lesson_id', 'name', 'position', 'video', 'ppt', 'Notes')