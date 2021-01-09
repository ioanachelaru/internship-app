from django.db import models
from knox.auth import User


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    cv = models.FileField(blank=True, null=True, default=None, upload_to='./cvs')
    # user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True)
