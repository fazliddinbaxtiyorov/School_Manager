from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy


from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, 'Your account has been registered.')
                return redirect('/')
            else:
                messages.error(request, 'Failed to authenticate user.')
        else:
            messages.error(request, 'Invalid form submission.')
    else:
        form = UserRegisterForm()
    return render(request, 'sign.html', {'form': form})


class Login(LoginView):
    template_name = 'login.html'

    def get_success_url(self):

        return reverse_lazy('adminpage')

