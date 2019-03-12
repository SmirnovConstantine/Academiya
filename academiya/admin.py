from django.contrib import admin

# Register your models here.

from .models import Planet, Test_task, Answers, Master

admin.site.register(Planet)
admin.site.register(Test_task)
admin.site.register(Answers)
admin.site.register(Master)
