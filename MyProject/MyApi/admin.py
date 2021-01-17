from django.contrib import admin
from .models import Project, Event
from import_export.admin import ImportExportModelAdmin


# Register your models here.
def make_staff(modeladmin, request, queryset):
    queryset.update(is_staff=True)
    make_staff.short_description = "Mark selected users as staff"


class UserAdmin(admin.ModelAdmin):
    actions = [make_staff]


@admin.register(Project)
class ProjectAdmin(ImportExportModelAdmin):
    search_fields = ('name',)
    list_display = ("name", "git_url", "user")
    pass


@admin.register(Event)
class EventAdmin(ImportExportModelAdmin):
    search_fields = ('name',)
    list_display = ("name", "city", "user")
    pass
