from django.db import models
from django_currentuser.db.models import CurrentUserField
from knox.auth import User
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    cv = models.FileField(blank=True, null=True, default=None, upload_to='./cvs')
    # user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True)


class Hr(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    # company_id = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True)


class Company(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1000)
    logo = models.ImageField(blank=True, default=None, upload_to='./logos')


class Announcement(models.Model):
    id_ann = models.AutoField(primary_key=True)
    company = models.OneToOneField(Company, unique=True, on_delete=models.CASCADE)
    job_name = models.CharField(max_length=200)
    job_description = models.CharField(max_length=1000)
    deadline = models.DateField()


class JobApplication(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    announcement = models.OneToOneField(Announcement, on_delete=models.CASCADE)
    attachments = models.FileField(blank=True, null=True, default=None, upload_to='./attachments')
    date = models.DateTimeField(auto_now=True)
    created_by = get_current_authenticated_user
    
    class Meta:
        unique_together = ('student', 'announcement',)
