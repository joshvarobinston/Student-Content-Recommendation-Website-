from django.urls import path
from api.views.auth import SignupView, LoginView

urlpatterns = [
    path("auth/signup/", SignupView.as_view()),
    path("auth/login/", LoginView.as_view()),
]
