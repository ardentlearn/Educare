from .models import Questions
from django import forms
from django.contrib.auth.forms import UserCreationForm


class QuestionUpdateForm(forms.ModelForm):
    class Meta:
        model = Questions

        fields = "__all__"
