from .models import Questions, Quiz
from django import forms
from django.contrib.auth.forms import UserCreationForm


class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Questions

        fields = "__all__"


class CreateQuizForm(forms.ModelForm):
    class Meta:
        model = Quiz

        fields = ["quiz_name"]
