from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from inscription.forms import InscriptionForm

def signup(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
    else:
        form = InscriptionForm()
    return render(request, 'inscription.html', {'form': form})
