from django.shortcuts import render
from mopga.modules.search.forms import SearchProjectForm
from mopga.modules.projet.models import Projects
from mopga.modules.user.models import User


def search(request):
    projects = Projects.objects.all()
    if request.method == 'POST':
        form = SearchProjectForm(request.POST)
        title = request.POST.get('title')

        # TODO Filtrage par date

        # deadlineMin = request.POST.get('deadlinemin')
        # deadlineMax = request.POST.get('deadlinemax')
        donationGoalMin = request.POST.get('donationgoalmin')
        donationGoalMax = request.POST.get('donationgoalmin')
        donationRateMin = request.POST.get('donationRateMin')
        donationRateMax = request.POST.get('donationRateMax')
        makerKarmaMin = request.POST.get('makerKarmaMin')
        makerKarmaMax = request.POST.get('makerKarmaMax')
        ratingMin = request.POST.get('ratingmin')
        ratingMax = request.POST.get('ratingmax')

        if title is not None:
            projects = projects.filter(title__contains=title)

        # TODO Filtrage par date

        # if deadlineMin is not None:
        #     projects = projects.filter(deadline__gte=deadlineMin)
        # if deadlineMax is not None:
        #     projects = projects.filter(deadline__lte=deadlineMax)

        if donationGoalMin is not None and donationGoalMin != '':
            projects = projects.filter(donationGoal__gte=donationGoalMin)
        if donationGoalMax is not None and donationGoalMax != '':
            projects = projects.filter(donationGoal__lte=donationGoalMax)
        if ratingMax is not None and ratingMax != '':
            projects = projects.filter(score__gte=ratingMax)
        if ratingMin is not None and ratingMin != '':
            projects = projects.filter(score__lte=ratingMin)
        if makerKarmaMin is not None and makerKarmaMin != '':
            projects = projects.filter(annoncer__karma__gte=makerKarmaMin)
        if makerKarmaMax is not None and makerKarmaMax != '':
            projects = projects.filter(annoncer__karma__lte=makerKarmaMax)
        if donationRateMin is not None and donationRateMin != '':
            projects = filterprojectsbypercentagefundedmin(projects, donationRateMin)
        if donationRateMax is not None and donationRateMax != '':
            projects = filterprojectsbypercentagefundedmax(projects, donationRateMin)
    else:
        form = SearchProjectForm()
    return render(request, 'search.html', {'form': form, 'projects': projects})

def filterprojectsbypercentagefundedmin(p, min):
    res = list(p)
    for r in res:
        if r.percentageFunded() < int(min):
            res.remove(r)

    return res

def filterprojectsbypercentagefundedmax(p, max):
    res = list(p)
    for r in res:
        if r.percentageFunded() > int(max):
            res.remove(r)

    return res

