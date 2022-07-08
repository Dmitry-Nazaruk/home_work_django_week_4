from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse_lazy, reverse
from django.views.generic import FormView, TemplateView
from django.views import View

# Create your views here.
from .forms import ReviewForm
from bookstore.models import Books


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = reverse_lazy('base')
    template_name = 'registration/register.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = reverse_lazy('base')

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('base'))



# class Review(TemplateView):
#     template_name = 'review.html'


class Create_Review(FormView):
    form_class = ReviewForm
    template_name = 'create_review.html'
    success_url = reverse_lazy('base')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


