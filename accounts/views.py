from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView as DLoginView

from .forms import UserCreationForm


class LoginView(DLoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'


class RegisterView(CreateView):
    model = User
    template_name = 'accounts/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('movies:homepage')

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        messages.success(self.request, 'Registered Successfully!')
        return response
