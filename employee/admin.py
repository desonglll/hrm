from django.contrib import admin

from employee.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = (
        "username",
        "email",
        "first_name",
        "last_name",
        "department",
        "position",
        "is_staff",
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        # 超级管理员可以查看所有员工
        if request.user.is_superuser:
            return qs
        # 普通员工只能查看自己
        return qs.filter(pk=request.user.pk)

    def has_change_permission(self, request, obj=None):
        # 超级管理员可以修改任何员工
        if request.user.is_superuser:
            return True
        # 如果操作对象为空（比如列表页请求），允许
        if obj is None:
            return True
        # 普通员工只能修改自己的信息
        return obj.pk == request.user.pk

    def has_delete_permission(self, request, obj=None):
        # 禁止普通员工删除
        if request.user.is_superuser:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        # 超级管理员可以查看所有
        if request.user.is_superuser:
            return True
        # 普通员工只能查看自己
        if obj is None:
            # 列表页允许，但 get_queryset 过滤了只能看到自己
            return True
        return obj.pk == request.user.pk

    # 禁用添加权限，员工不能新增用户
    def has_add_permission(self, request):
        return request.user.is_superuser
