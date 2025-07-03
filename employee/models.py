from django.db import models
from django.contrib.auth.models import AbstractUser
from uuid import uuid4


class Employee(AbstractUser):
    id = models.UUIDField(
        verbose_name="编号",
        primary_key=True,
        default=uuid4,
        editable=False,
    )
    age = models.PositiveIntegerField(verbose_name="年龄", default=18)
    department = models.ForeignKey(
        "department.Department",
        verbose_name="所属部门",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    position = models.ForeignKey(
        "department.Position",
        verbose_name="职位名称",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    createdAt = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    updatedAt = models.DateTimeField(verbose_name="更新时间", auto_now=True)

    class Meta:
        verbose_name = "员工信息"
        verbose_name_plural = "员工信息"
