from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from adminBlog.forms import *


# Create your views here.
class Login(LoginView):
    form_class = AuthUserFrom
    template_name = 'adminBlog/login.html'

    def get(self, request, *args, **kwargs):
        if request.session.get_expiry_age() > 0:
            if request.user.is_authenticated:
                return redirect('home:index')
            else:
                logout(request)
        return super().get(request, *args, **kwargs)

    def form_valid(self, form):
        remember_me = form.cleaned_data['remember_me']
        if remember_me:
            self.request.session.set_expiry(60 * 60 * 24 * 30)
        else:
            self.request.session.set_expiry(0)
        return super(Login, self).form_valid(form)

    def form_invalid(self, form):
        return render(self.request, self.template_name, {'form': form})

    def get_success_url(self):
        self.success_url = reverse_lazy('home:index')
        return self.success_url


def register(request):
    return render(request, 'adminBlog/register.html')


def reset_password(request):
    return render(request, 'adminBlog/reset-password.html')
