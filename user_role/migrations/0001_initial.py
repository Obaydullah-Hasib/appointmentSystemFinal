# Generated by Django 4.2.6 on 2023-10-31 09:18

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="roleTable",
            fields=[
                ("roleID", models.AutoField(primary_key=True, serialize=False)),
                ("roleName", models.CharField(max_length=255)),
            ],
        ),
    ]
