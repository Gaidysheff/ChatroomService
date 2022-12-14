from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfileForm, PasswordChangingForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    # form_class = PasswordChangeForm
    template_name = "registration/change_password.html"
    success_url = reverse_lazy("password_success")


def password_success(request):
    return render(request, "registration/password_success.html", {})


class UserRegistrationView(generic.CreateView):
    form_class = SignUpForm
    template_name = "registration/registration.html"
    success_url = reverse_lazy("login")


class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = "registration/edit_profile.html"
    success_url = reverse_lazy("home")

    def get_object(self):
        return self.request.user
