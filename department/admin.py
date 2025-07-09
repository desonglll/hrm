from django.contrib import admin

from department.models import Department, Position


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    pass


@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    pass
