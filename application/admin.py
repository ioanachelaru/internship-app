from django.contrib import admin
from application.models import Student, Company, Hr, JobApplication, Announcement

# Register your models here.
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Hr)
admin.site.register(JobApplication)
admin.site.register(Announcement)
