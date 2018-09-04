from django.contrib.auth.views import LoginView as DLoginView


class LoginView(DLoginView):
    redirect_authenticated_user = True
    template_name = 'accounts/login.html'
