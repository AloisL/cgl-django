from django.contrib.auth import login
from django.shortcuts import render, redirect

from mopga.modules.projet.models import Projects
from mopga.modules.user.forms import RegisterForm, FundsForm, UpdateForm
from mopga.modules.user.models import User


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def modifProfile(request):
    user = request.user
    fundsForm = FundsForm()
    form = UpdateForm(initial={
        "description": user.description,
        "role": user.role,
        "email": user.email,
    })
    if request.method == 'POST' and "userform":
        print('post userform')
        form = UpdateForm(request.POST)
        if form.is_valid():
            user.description = form.cleaned_data['description']
            user.email = form.cleaned_data['email']
            user.role = form.cleaned_data['role']
            user.save()
            return redirect('/profile')
    if request.method == 'POST' and "fundsform":
        print('post fundform')
        form = FundsForm(request.POST)
        if form.is_valid():
            addedfunds = form.cleaned_data['addfunds']
            user.add_funds(addedfunds)
            user.save()
            return redirect('/profile')
    print('get')
    args = {
        'form': form,
        'fundsForm': fundsForm,
        'user': user
    }
    print(args)
    return render(request, 'profile.html', args)


def userProjects(request):
    if request.user.is_authenticated:
        projects = Projects.objects.filter(annoncer_id=request.user.pk)
        args = {
            'projects': projects
        }
        return render(request, 'userprojects.html', args)
    else:
        return render(request, 'home.html')


def showProfile(request, username):
    if username != None:
        usershowed = User.objects.get(username=username)
        if request.method == 'POST' and "minus" in request.POST:
            print("POST MINUS")
            usershowed.karma -= 1
            usershowed.save()
        if request.method == 'POST' and "plus" in request.POST:
            print("POST PLUS")
            usershowed.karma += 1
            usershowed.save()
        args = {
            'user': request.user,
            'usershowed': usershowed
        }
        return render(request, 'showprofile.html', args)
    else:
        return redirect('/')
