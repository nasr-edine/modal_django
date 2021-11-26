from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import TemplateView
from django.views.generic import UpdateView
from .forms import CustomUserCreationForm, UserForm

from .models import CustomUser


class HomePageView(TemplateView):
    template_name = 'home.html'


class ChangeEmailView(UpdateView):
    model = CustomUser
    form_class = UserForm
    success_url = reverse_lazy('home')
    template_name = 'change_email.html'


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
