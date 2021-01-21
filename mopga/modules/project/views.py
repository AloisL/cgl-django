import os

from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.utils.timezone import localtime, now

from .forms import NewProject, NewComment, AddNote, AddFundsProject
from .models import Projects, Image, Comments, EvaluateBy


# Create your views here.

# Un nouveau project
def new_project(request):
    if request.user.is_anonymous:
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


##Affichage du project à l'id en paramètres
def project(request, projectId=1):
    allComments = None
    msgError = None
    try:
        project = Projects.objects.get(pk=projectId)
        allComments = Comments.objects.filter(project=project).order_by('-id')

        if request.method == 'POST' and 'fundsProjectForm' in request.POST:
            formAddFunds = AddFundsProject(request.POST)
            if formAddFunds.is_valid():
                fundsToProject = formAddFunds.cleaned_data['addfunds']
                if request.user.funds < fundsToProject:
                    msgError = "Insufficient funds, click here to add funds."
                else:
                    request.user.funds -= fundsToProject
                    project.moneyCollected += fundsToProject
                    request.user.save()
                    project.save()
        if request.method == 'POST' and 'voteProjectForm' in request.POST:
            if checkKarma(request.user):
                evaluations = EvaluateBy.objects.all().filter(idProject=project, idUser=request.user.id)
                if len(evaluations) == 0:
                    score = request.POST.get('notation')
                    evaluate = EvaluateBy(
                        idProject=project,
                        idUser=request.user,
                        score=score
                    )
                    evaluate.save()
                    project.note = project.get_score()
                    project.save()

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
    except Projects.DoesNotExist:
        project = None
    form = NewComment()
    voteForm = AddNote()
    fundsForm = AddFundsProject()

    if request.path.startswith("/project"):
        projectpage = True
    else:
        projectpage = False

    args = {
        'projectId': projectId,
        'project': project,
        'form': form,
        'comments': allComments,
        'voteForm': voteForm,
        'formFunds': fundsForm,
        'msgError': msgError,
        'user': request.user,
        'projectpage': projectpage
    }

    return render(request, 'project.html', args)


def modifproject(request, projectId=1):
    try:
        project = Projects.objects.get(pk=projectId)
        if request.user.is_anonymous == True:
            response = redirect('/')
            return response
        if request.user.id == project.annoncer.id:
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


def checkKarma(user):
    if user.karma >= 50:
        return True
    else:
        return False


def top(request):
    topprojects = Projects.objects.all().order_by('-note')[:5]
    args = {'topprojects': topprojects,
            'path': request.path}
    return render(request, 'top.html', args)
