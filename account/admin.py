from django.contrib import admin
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass

# @admin.register(Session)
# class SessionAdmin(admin.ModelAdmin):
#     pass
#

@admin.register(ContentType)
class ContentTypeAdmin(admin.ModelAdmin):
    pass