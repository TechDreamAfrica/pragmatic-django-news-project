from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Reporters)
admin.site.register(Categories)
admin.site.register(Articles)
admin.site.register(Images)
admin.site.register(Videos)