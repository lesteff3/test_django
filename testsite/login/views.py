from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import SignUpForm
from .models import Profile

from django.core.mail import EmailMessage

def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # сохранение номера
            Profile.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'login/regist.html', {'form': form})



class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'books/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')



