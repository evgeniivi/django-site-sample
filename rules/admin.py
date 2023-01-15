from django.contrib import admin

# Register your models here.

from .models import ufoslide
from .models import menuitem
from .models import merch
from .models import post

admin.site.register(ufoslide)
admin.site.register(menuitem)
admin.site.register(merch)
admin.site.register(post)