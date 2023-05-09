from django.contrib import admin
from .models import Forward, Option


class OptionInline(admin.TabularInline):
    model = Option


class ForwardAdmin(admin.ModelAdmin):
    inlines = [
        OptionInline,
    ]


admin.site.register(Forward, ForwardAdmin)

admin.site.register(Option)
