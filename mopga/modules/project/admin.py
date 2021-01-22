from django.contrib import admin

from mopga.modules.project.models import Project, Comment, Image, EvaluateBy

admin.site.register(Project)
admin.site.register(Comment)
admin.site.register(Image)
admin.site.register(EvaluateBy)