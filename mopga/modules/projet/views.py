from django.shortcuts import render, redirect
from .forms import NewProject
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
            query = Project(
                title = title,
                description = description,
                deadline = deadline,
                donationGoal = donationGoal,
                annoncer_id = user.id,
                beginDate = beginDate
            )
            query.save()
            response = redirect('/new_project/')
            return response
    else:
        form = NewProject()
    return render(request, 'new_project.html', {'form': form})