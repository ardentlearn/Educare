from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = "accounts"

urlpatterns = [
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(next_page="accounts:login"), name="logout"),
    path("registration/", views.RegistrationPageView.as_view(), name="registration"),
    path("profile/<int:pk>/", views.UserUpdateView.as_view(), name="profile"),
]
