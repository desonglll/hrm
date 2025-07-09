import openpyxl
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http.response import HttpResponse
from django.utils.html import format_html

from employee.models import Employee


@admin.action(description="导出选中用户为 Excel")
def export_selected_employees(modeladmin, request, queryset):
    # 1. 指定要导出的字段（按需自定义）
    fields = [
        ("username", "用户名"),
        ("first_name", "名"),
        ("last_name", "姓"),
        ("email", "邮箱"),
        ("age", "年龄"),
        ("department__name", "部门"),  # 如果是外键
        ("position__name", "职位"),  # 如果是外键
    ]

    # 2. 创建 Excel 工作簿
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "员工数据"

    # 3. 写入表头
    ws.append([header for _, header in fields])

    # 4. 写入数据
    for obj in queryset:
        row = []
        for field_path, _ in fields:
            parts = field_path.split("__")
            value = obj
            for part in parts:
                value = getattr(value, part, "")
                if callable(value):
                    value = value()
            row.append(value)
        ws.append(row)

    # 5. 返回 Excel 文件
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = 'attachment; filename=selected_employees.xlsx'
    wb.save(response)
    return response


@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    actions = [export_selected_employees]
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (
            "个人信息",
            {
                "fields": (
                    "photo_preview",
                    "photo",
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

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" style="max-height: 99px;"/>', obj.photo.url)
        return "-"

    photo_preview.short_description = '预览图'

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
                        "photo_preview",
                        "photo",
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
            return super().get_readonly_fields(request, obj) + ("photo_preview",)
        return (
            "photo_preview",
            "department",
            "position",
        )
