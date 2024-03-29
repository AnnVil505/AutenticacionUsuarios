# Generated by Django 4.2.1 on 2023-06-04 19:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Permission",
            fields=[
                (
                    "id_permission",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                ("name_permission", models.CharField(max_length=100)),
                ("description_permission", models.TextField(max_length=1000)),
                ("date_permission", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Role",
            fields=[
                ("id_role", models.BigAutoField(primary_key=True, serialize=False)),
                ("name_role", models.CharField(max_length=40)),
                ("description_role", models.TextField(max_length=1000)),
                ("date_role", models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Role_User",
            fields=[
                (
                    "id_role_user",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                (
                    "id_role_FK",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Autenticacion.role",
                    ),
                ),
                (
                    "id_user_FK",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Role_Permission",
            fields=[
                (
                    "id_role_permission",
                    models.BigAutoField(primary_key=True, serialize=False),
                ),
                (
                    "id_permission_FK",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Autenticacion.permission",
                    ),
                ),
                (
                    "id_role_FK",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Autenticacion.role",
                    ),
                ),
            ],
        ),
    ]
