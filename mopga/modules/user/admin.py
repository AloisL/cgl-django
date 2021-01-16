from django.contrib import admin

# Register your models here.

from mopga.modules.user.models import User

admin.site.register(User)
