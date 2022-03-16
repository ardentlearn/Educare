from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import User
from .forms import CreateUserForm


class HomePageView(TemplateView):
    template_name = "home.html"


class RegistrationPageView(CreateView):
    template_name = "accounts/registration.html"
    form_class = CreateUserForm

    def form_valid(self, form):
        messages.success(self.request, "Account created")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("accounts:login")

class CustomLoginView(LoginView):
    template_name = "accounts/login.html"
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("curriculum:branch_list")

class UserUpdateView(UpdateView):
    template_name = "accounts/profile.html"
    form_class = CreateUserForm
    queryset = User.objects.all()

    def form_valid(self, form):
        messages.success(self.request, "Account Updated")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse("home")
