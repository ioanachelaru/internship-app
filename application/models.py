from django.db import models
from django_currentuser.db.models import CurrentUserField
from django_currentuser.middleware import (
    get_current_user, get_current_authenticated_user)
from django.contrib.auth.models import AbstractUser, Permission

class ApplicationUser(AbstractUser):
    def make_student(self, name, email):
        self.is_staff = True
        self.is_superuser = False
        self.user_permissions.set([
            Permission.objects.get(codename='view_announcement'),
        ])
        self.save()
        Student.objects.create(
            user = self,
            username = self.username,
            password = self.password,
            name = name,
            email = email,
        )

    def make_hr(self):
        self.is_staff = True
        self.is_superuser = False
        self.user_permissions.set([
            Permission.objects.get(codename='view_announcement'),
            Permission.objects.get(codename='add_announcement'),
            Permission.objects.get(codename='change_announcement'),
            Permission.objects.get(codename='delete_announcement'),
            Permission.objects.get(codename='view_company'),
            Permission.objects.get(codename='add_company'),
            Permission.objects.get(codename='change_company'),
            Permission.objects.get(codename='delete_company'),
        ])
        self.save()

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(ApplicationUser, unique=True, on_delete=models.CASCADE)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    cv = models.FileField(blank=True, null=True, default=None, upload_to='./cvs')
    # user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE, null=True)


class Hr(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(ApplicationUser, unique=True, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.name


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
