
# Create your models here.
from django.db import models
from user_role.models import roleTable
class userModel(models.Model):
    id = models.AutoField(primary_key=True)
    uname = models.CharField(max_length=255)
    user_first_name = models.CharField(max_length=50)
    user_last_name = models.CharField(max_length=50)
    user_email = models.CharField(max_length=255)
    user_roleID = models.ForeignKey(roleTable, on_delete=models.CASCADE)
    user_profile_pic = models.ImageField(null=True, blank=True, upload_to ="images/")
    password = models.CharField(max_length = 100,null=False)
    verification_code = models.CharField(max_length=35)
    verified = models.BooleanField(default=False,null=False)
