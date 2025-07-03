from django.db import models


# Create your models here.
class OrgUnit(models.Model):
    name = models.CharField(verbose_name="组织层级", max_length=100)
    type = models.CharField(
        verbose_name="类型", max_length=50
    )  # e.g., 'Company', 'Division', 'Department'
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    leaders = models.ManyToManyField(
        "employee.Employee",
        verbose_name="管理人员",
        blank=True,
        related_name="managed_units",
    )

    class Meta:
        verbose_name = "组织层级信息"
        verbose_name_plural = "组织层级信息"

    pass
