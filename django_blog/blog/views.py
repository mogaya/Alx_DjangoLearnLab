from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationform

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationform(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration Successful")
            return redirect('profile')
        else:
            form = UserRegistrationform()
    return render(request, 'blog/register.html', {'form':form})
    
@login_required
def profile(request):
    return render(request, 'blog/profile.html')
