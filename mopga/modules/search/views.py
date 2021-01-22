from django.shortcuts import render, redirect

from mopga.modules.project.models import Project
from mopga.modules.search.forms import SearchProjectForm


def search(request):
    if request.user.is_anonymous:
        return redirect('/')

    projects = None
    if request.method == 'POST':
        projects = Project.objects.all()
        form = SearchProjectForm(request.POST)
        title = request.POST.get('title')
        donationGoalMin = request.POST.get('donationGoalMin')
        donationGoalMax = request.POST.get('donationGoalMax')
        donationRateMin = request.POST.get('donationRateMin')
        donationRateMax = request.POST.get('donationRateMax')
        makerKarmaMin = request.POST.get('makerKarmaMin')
        makerKarmaMax = request.POST.get('makerKarmaMax')
        ratingMin = request.POST.get('ratingmin')
        ratingMax = request.POST.get('ratingmax')

        if title is not None:
            projects = projects.filter(title__contains=title)

        if donationGoalMin is not None and donationGoalMin != '':
            projects = projects.filter(donationGoal__gte=donationGoalMin)
        if donationGoalMax is not None and donationGoalMax != '':
            projects = projects.filter(donationGoal__lte=donationGoalMax)
        if makerKarmaMin is not None and makerKarmaMin != '':
            projects = projects.filter(annoncer__karma__gte=makerKarmaMin)
        if makerKarmaMax is not None and makerKarmaMax != '':
            projects = projects.filter(annoncer__karma__lte=makerKarmaMax)
        if ratingMax is not None and ratingMax != '':
            projects = filterprojectsbyratingmax(projects, ratingMax)
        if ratingMin is not None and ratingMin != '':
            projects = filterprojectsbyratingmin(projects, ratingMin)
        if donationRateMin is not None and donationRateMin != '':
            projects = filterprojectsbypercentagefundedmin(projects, donationRateMin)
        if donationRateMax is not None and donationRateMax != '':
            projects = filterprojectsbypercentagefundedmax(projects, donationRateMax)
    else:
        form = SearchProjectForm()
    return render(request, 'search.html', {'form': form, 'projects': projects, 'path': request.path})


def filterprojectsbypercentagefundedmin(proj, minimum):
    res = []
    for p in proj:
        if float(p.percentageFunded()) >= float(minimum):
            res.append(p)
    return res


def filterprojectsbypercentagefundedmax(proj, maximum):
    res = []
    for p in proj:
        if float(p.percentageFunded()) <= float(maximum):
            res.append(p)

    return res


def filterprojectsbyratingmax(proj, ratMax):
    res = []
    for p in proj:
        if p.get_score() <= float(ratMax):
            res.append(p)

    return res


def filterprojectsbyratingmin(proj, ratMin):
    res = []
    for p in proj:
        if p.get_score() >= float(ratMin):
            res.append(p)
    return res
