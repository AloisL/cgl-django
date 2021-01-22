from django.contrib import admin

from mopga.modules.project.models import Projects, Comments, Image, EvaluateBy

admin.site.register(Projects)
admin.site.register(Comments)
admin.site.register(Image)
admin.site.register(EvaluateBy)