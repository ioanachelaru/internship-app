from django.db import models
# from knox.auth import User


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    cv = models.FileField(blank=True, null=True, default=None, upload_to='./cvs')
    # user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True)


class Hr(models.Model):
    id = models.AutoField(primary_key=True)
    # id_company = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True)
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
    # id_company = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True)
    job_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    job_description = models.CharField(max_length=1000)
    deadline = models.DateField()


class Job_appl(models.Model):
    id = models.AutoField(primary_key=True)
    # id_student = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True, default=None)
    attachments = models.FileField(blank=True, null=True, default=None, upload_to='./attachments')
    date = models.DateTimeField(auto_now=True)
