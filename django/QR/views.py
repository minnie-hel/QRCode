from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import StudentRegistrationForm, StudentLoginForm
from .models import Student





def register(request):
    if request.method == 'POST':
        form = StudentRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()  # Password is hashed in forms.py
            messages.success(request, "Registration successful.")
            return redirect('login')
        else:
            messages.error(request, "Registration failed.")
    else:
        form = StudentRegistrationForm()

    return render(request, 'register.html', {'form': form})

def user_login(request):
    form = StudentLoginForm(request.POST)
    
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)

            return redirect(dashboard)
           
    return render(request, "login.html", {"form": form})

    

          
  


