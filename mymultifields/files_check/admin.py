from django.contrib import admin
from .models import DocCheck, CheckerFiles


class DocCheckAdmin(admin.ModelAdmin):
    list_display = ['title', 'file_mssp', 'file_quotes']


class CheckerFilesAdmin(admin.ModelAdmin):
    list_display = ['title', 'dock_check', 'result']


admin.site.register(DocCheck, DocCheckAdmin)
admin.site.register(CheckerFiles, CheckerFilesAdmin)
