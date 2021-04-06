from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView, CreateView, TemplateView
from .models import User


class HomePageView(TemplateView):
    template_name = 'home.html'


class RegistrationPageView(CreateView):
    template_name = 'accounts/registration.html'
    form_class = CreateUserForm

    def form_valid(self, form):
        messages.success(self.request, "Account created")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('accounts:login')


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            email = request.POST.get('email')
            password = request.POST.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Invalid credentials")

        return render(request, 'accounts/login.html')


def logout_page(request):
    logout(request)
    return redirect('/')


class UserUpdateView(UpdateView):
    template_name = 'accounts/profile.html'
    form_class = CreateUserForm
    queryset = User.objects.all()

    def form_valid(self, form):
        messages.success(self.request, "Account Updated")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('home')
