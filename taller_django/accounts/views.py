
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib.auth import login, authenticate

from accounts.forms import SignupForm

class SignupView(FormView):
    def get(self, request):
        form = SignupForm()

        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=password)

            login(request, user)

            return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'form': form})

class LoginView(BaseLoginView):
    template_name = 'accounts/login.html'
