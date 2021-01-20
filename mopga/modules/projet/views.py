import os

from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.utils.timezone import localtime, now

from .forms import NewProject, NewComment
from .models import Projects, Image, Comments


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
    comments(request, projectId)
    return render(request, 'project.html', args)


def comments(request, projectId=1):
    the_project = Projects.objects.get(pk=projectId)
    comments = Comments.objects.filter(project=the_project)
    if request.method == 'POST' and 'commentForm' in request.POST:
        formComment = NewComment(request.POST)
        if formComment.is_valid():
            user = request.user
            title = formComment.cleaned_data['title']
            content = formComment.cleaned_data['content']
            beginDate = localtime(now())
            # MAJ Comment
            comment = Comments(
                title=title,
                content=content,
                user=user,
                project=project,
                beginDate=beginDate
            )
            comment.save()

            response = redirect('/project/' + str(project.id))
            return response
    else:
        print('form')
        form = NewComment()

        arg = {'comments': comments,
               'form': form}
    return render(request, 'comments.html', {'form': form})


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
                        project.title = title
                        project.description = description
                        project.deadline = deadline
                        project.donationGoal = donationGoal
                        project.save()
                        # TODO IMAGE modifable
                        # TODO ajouter Button Delete
                        response = redirect('/project/' + str(project.id))
                        return response
                    except IntegrityError as e:
                        if str(e).endswith("projects.title"):
                            form = NewProject()
                            return render(request, 'modif_project.html',
                                          {'error': "Project already existing", 'form': form})
                        render(request, 'modif_project.html', {'form': form})
            else:
                form = NewProject(initial={"title": project.title,
                                           "description": project.description,
                                           "donationGoal": project.donationGoal,
                                           "deadline": project.deadline
                                           })
                return render(request, 'modif_project.html', {'form': form})
        else:
            return redirect('/project/' + projectId)
    except Projects.DoesNotExist:
        msgError = "Project doesn't exist"

    return redirect('/', {'msgError', msgError})
