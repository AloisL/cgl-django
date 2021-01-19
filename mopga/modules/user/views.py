from django.contrib.auth import login
from django.shortcuts import render, redirect

from mopga.modules.user.forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def modifProfile(request):
    user=request.user
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm(initial={"username":user.username,
                                     "description":user.description,
                                     "role":user.role,
                                     "email":user.email,
                                     "password1":user.password,
                                     "password2": user.password})
    return render(request, 'profile.html', {'form': form})