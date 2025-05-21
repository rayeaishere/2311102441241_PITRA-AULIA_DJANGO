from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Registration successful. You can now log in.')
            return redirect('login')  # pastikan kamu punya URL 'login'
    else:
        form = RegisterForm()
    return render(request, 'accounts/register.html', {'form': form})

