from django.contrib import admin

# Register your models here.
# admin/123456


from django.contrib import admin
from .models import Question
from .models import DocsLinux

admin.site.register(Question)
admin.site.register(DocsLinux)