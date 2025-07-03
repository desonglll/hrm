from django.db import models
from uuid import uuid4


class Department(models.Model):
    id = models.UUIDField(
        verbose_name="编号", null=False, default=uuid4(), primary_key=True
    )
    # number = models.CharField(
    #     max_length=20,
    #     unique=True,
    # )
    name = models.CharField(verbose_name="部门名称", blank=False)
    createdAt = models.DateTimeField(verbose_name="创建时间", auto_now=True)
    updatedAt = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = "部门信息"
        verbose_name_plural = "部门信息"

    pass


class Position(models.Model):
    id = models.UUIDField(
        verbose_name="编号", null=False, default=uuid4(), primary_key=True
    )
    name = models.CharField(verbose_name="职位名称", blank=False)
    createdAt = models.DateTimeField(verbose_name="创建时间", auto_now=True)
    updatedAt = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = "职位信息"
        verbose_name_plural = "职位信息"

    pass
