"""mopga URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import path
from django.views.generic.base import RedirectView

from mopga.modules.home.views import home
from mopga.modules.project.views import new_project, project, modifproject, top
from mopga.modules.search.views import search
from mopga.modules.user.views import register, modifProfile, userProjects, showProfile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('new_project', new_project),
    path('project/<int:projectId>/', project),
    path('modifproject/<int:projectId>/', modifproject),
    path('userprojects', userProjects),
    path('register', register),
    path('profile', modifProfile),
    path('profile/<str:username>/', showProfile),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('search', search),
    path('top', top),
    path(
        "favicon.ico",
        RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    )
]
