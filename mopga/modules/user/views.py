from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from mopga.modules.user.forms import InscriptionForm


def register(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = InscriptionForm()
    return render(request, 'register.html', {'form': form})
