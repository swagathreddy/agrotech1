from django.contrib import admin
from .models import Farm,Farmer,Blog

admin.site.register(Farm)
admin.site.register(Farmer)
admin.site.register(Blog)

from django.contrib import admin
from .models import Question,Answer,Comment
# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Comment)