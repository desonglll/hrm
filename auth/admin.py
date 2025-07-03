from django.contrib.auth.models import User, Group, Permission
from django.contrib import admin

admin.site.unregister(User)
admin.site.unregister(Group)


class CustomUserAdmin(admin.ModelAdmin):

    pass


class CustomGroupAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, CustomUserAdmin)
admin.site.register(Group, CustomGroupAdmin)

User._meta.verbose_name = "用户"
User._meta.verbose_name_plural = "用户"
Group._meta.verbose_name = "用户组"
Group._meta.verbose_name_plural = "用户组"
Permission._meta.verbose_name = "权限"
Permission._meta.verbose_name_plural = "权限"
