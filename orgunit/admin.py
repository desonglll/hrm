from django.contrib import admin
from orgunit.models import OrgUnit


@admin.register(OrgUnit)
class OrgUnitAdmin(admin.ModelAdmin):
    pass
