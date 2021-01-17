from django.shortcuts import render, redirect
from django.utils.timezone import localtime, now

from .forms import NewProject
from .models import Projects


# Create your views here.

# Un nouveau projet
def new_project(request):
    if request.user.is_anonymous == True:
        response = redirect('/')
        return response

    if request.method == 'POST':
        form = NewProject(request.POST)
        if form.is_valid():
            user = request.user
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            donationGoal = form.cleaned_data['donationGoal']
            deadline = form.cleaned_data['deadline']
            beginDate = localtime(now())
            query = Projects(
                title=title,
                description=description,
                deadline=deadline,
                donationGoal=donationGoal,
                annoncer_id=user.id,
                beginDate=beginDate
            )
            query.save()
            # TODO : redirection vers le projet
            response = redirect('/')
            return response
    else:
        form = NewProject()
    return render(request, 'new_project.html', {'form': form})


##Affichage du projet à l'id en paramètres
def project(request, projectId=1):
    try:
        project = Projects.objects.get(pk=projectId)
        try:
            projectComments = project.comment_set.all().order_by('-post_date')
        except Comment.DoesNotExist:
            projectComments = None
    except Projects.DoesNotExist:
        project = None
        projectComments = None

    ## Gestion du formulaire
    formDonation = None
    formComment = None
    formNote = None
    if request.user.is_anonymous == False:
        if request.method == 'POST' and 'donationForm' in request.POST:
            formDonation = NewDonation(request.POST)
            if formDonation.is_valid():
                user = request.user
                montant = formDonation.cleaned_data['montant']
                # MAJ Donation
                query = Donation(
                    amount=montant,
                    donator_id=user.id,
                    project_id=projectId,
                    validated=False,
                )
                query.save()

                response = redirect('/cart/')
                return response
        else:
            formDonation = NewDonation()

        if request.method == 'POST' and 'commentForm' in request.POST:
            formComment = NewComment(request.POST)
            if formComment.is_valid():
                user = request.user
                title = formComment.cleaned_data['title']
                content = formComment.cleaned_data['content']

                # MAJ Comment
                query = Comment(
                    title=title,
                    content=content,
                    poster_id=user.id,
                    project_id=projectId,
                    karma=0,
                )
                query.save()

                formNote = NewNote()
                formComment = NewComment()
                formDonation = NewDonation()
        else:
            formComment = NewComment()

        if request.method == 'POST' and 'noteForm' in request.POST:
            formNote = NewNote(request.POST)
            if formNote.is_valid():
                user = request.user
                note = formNote.cleaned_data['note']

                if project.noteAmount == 0:
                    project.note = note
                    project.noteAmount = 1
                    project.save()
                else:
                    totalNotes = project.noteAmount;
                    newMoy = ((project.note * totalNotes) + note) / (totalNotes + 1)
                    project.note = newMoy
                    project.noteAmount = totalNotes + 1
                    project.save()

                formNote = NewNote()
                formComment = NewComment()
                formDonation = NewDonation()
        else:
            formNote = NewNote()

    projectOfConnectedUser = False
    connectedUserCanValidate = False
    if request.user.is_anonymous == False:
        if request.user.id == project.annoncer_id:
            projectOfConnectedUser = True
        if request.user.is_validator or request.user.is_staff:
            connectedUserCanValidate = True

    args = {
        'projectId': projectId,
        'project': project,
        'projectComments': projectComments,
        'formDonation': formDonation,
        'formComment': formComment,
        'formNote': formNote,
        'projectOfConnectedUser': projectOfConnectedUser,
        'connectedUserCanValidate': connectedUserCanValidate}
    return render(request, 'project.html', args)
