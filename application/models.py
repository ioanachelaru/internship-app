from django.db import models


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    cv = models.FileField(blank=True, null=True, default=None, upload_to='./cvs')
