from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationFrom


class SignUpView(CreateView):
    form_class = CustomUserCreationFrom
    success_url = reverse_lazy("login")
    template_name = "signup.html"
