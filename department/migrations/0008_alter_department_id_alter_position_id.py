# Generated by Django 5.2.4 on 2025-07-03 13:21

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('department', '0007_alter_department_id_alter_position_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a10308e4-5496-4976-8856-d3b4dc662938'), primary_key=True, serialize=False, verbose_name='编号'),
        ),
        migrations.AlterField(
            model_name='position',
            name='id',
            field=models.UUIDField(default=uuid.UUID('73bb4ddf-008e-4778-bdf8-3206a6dec3d0'), primary_key=True, serialize=False, verbose_name='编号'),
        ),
    ]
