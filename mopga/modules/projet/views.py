import os

from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.utils.timezone import localtime, now

from .forms import NewProject
from .models import Projects, Image


# Create your views here.

# Un nouveau projet
def new_project(request):
    if request.user.is_anonymous == True:
        response = redirect('/')
        return response

    if request.method == 'POST':
        form = NewProject(request.POST, request.FILES)
        if form.is_valid():
            try:
                user = request.user
                title = form.cleaned_data['title']
                description = form.cleaned_data['description']
                donationGoal = form.cleaned_data['donationGoal']
                deadline = form.cleaned_data['deadline']
                beginDate = localtime(now())
                img = form.cleaned_data['image']
                project = Projects(
                    title=title,
                    description=description,
                    deadline=deadline,
                    donationGoal=donationGoal,
                    annoncer_id=user.id,
                    beginDate=beginDate
                )
                project.save()
                image = Image(
                    projectId=project.id,
                    path=img
                )
                image.save()
                imgName = os.path.basename(os.path.normpath(image.path.url))
                project.setImageName(imgName)
                response = redirect('/project/' + str(project.id))
                return response
            except IntegrityError as e:
                if str(e).endswith("projects.title"):
                    form = NewProject()
                    return render(request, 'new_project.html', {'error': "Project already existing", 'form': form})
                render(request, 'new_project.html', {'form': form})
    else:
        form = NewProject()
    return render(request, 'new_project.html', {'form': form})


##Affichage du projet à l'id en paramètres
def project(request, projectId=1):
    try:
        project = Projects.objects.get(pk=projectId)

    except Projects.DoesNotExist:
        project = None


    args = {
        'projectId': projectId,
        'project': project,
    }
    return render(request, 'project.html', args)

def modifproject(request, projectId=1):
    try:
        project = Projects.objects.get(pk=projectId)
        if request.user.is_anonymous == True:
            response = redirect('/')
            return response
        if request.user.id == project.annoncer.id:
            print("annoncer")
            if request.method == 'POST':
                form = NewProject(request.POST, request.FILES)
                if form.is_valid():
                    try:
                        title = form.cleaned_data['title']
                        description = form.cleaned_data['description']
                        donationGoal = form.cleaned_data['donationGoal']
                        deadline = form.cleaned_data['deadline']
                        img = form.cleaned_data['image']
                        project.title=title
                        project.description=description
                        project.deadline=deadline
                        project.donationGoal=donationGoal
                        project.save()
                        #TODO IMAGE modifable
                        #TODO ajouter Button Delete
                        response = redirect('/project/' + str(project.id))
                        return response
                    except IntegrityError as e:
                        if str(e).endswith("projects.title"):
                            form = NewProject()
                            return render(request, 'modif_project.html', {'error': "Project already existing", 'form': form})
                        render(request, 'new_project.html', {'form': form})
            else:
                print("initial")
                form = NewProject(initial={"title":project.title,
                                           "description" : project.description,
                                           "donationGoal":project.donationGoal,
                                           "deadline": project.deadline
                                           })
                return render(request, 'new_project.html', {'form': form})
    except Projects.DoesNotExist:
        msgError = "Project doesn't exist"

    return redirect('/')