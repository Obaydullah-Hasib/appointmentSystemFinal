from django.db import models

# Create your models here.
class roleTable(models.Model):
    roleID = models.AutoField(primary_key=True)
    roleName=models.CharField(max_length=255)