from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from employee.models import Employee


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "个人信息",
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "email",
                    "age",
                    "department",
                    "position",
                )
            },
        ),
        (
            "权限",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("重要日期", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                ),
            },
        ),
    )
    list_display = ("username", "email", "first_name", "last_name", "is_staff")
    search_fields = ("username", "email", "first_name", "last_name")
    ordering = ("username",)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(pk=request.user.pk)

    def get_fieldsets(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_fieldsets(request, obj)
        return (
            (None, {"fields": ("username", "password")}),
            (
                "个人信息",
                {
                    "fields": (
                        "first_name",
                        "last_name",
                        "email",
                        "age",
                        "department",
                        "position",
                    )
                },
            ),
        )

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return super().get_readonly_fields(request, obj)
        return (
            "department",
            "position",
        )
