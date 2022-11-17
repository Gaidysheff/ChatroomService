from django.urls import path
from .views import UserRegistrationView, UserEditView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name="registration"),
    path("edit_profile/", UserEditView.as_view(), name="edit_profile"),
    path(
        "password/",
        auth_views.PasswordChangeView.as_view(
            template_name="registration/change_password.html"
        ),
    ),
]
