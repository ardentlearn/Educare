from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('registration/', views.RegistrationPageView.as_view(), name='registration'),
    path('profile/<str:pk>/', views.UserUpdateView.as_view(), name='profile'),
]
