from cmath import log
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Title)
admin.site.register(Tag)
admin.site.register(Explanation)
admin.site.register(User)
admin.site.register(Blog)