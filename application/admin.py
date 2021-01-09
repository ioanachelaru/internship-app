from django.contrib import admin
from application.models import Student, Company, Hr, Job_appl, Announcement

# Register your models here.
admin.site.register(Student)
admin.site.register(Company)
admin.site.register(Hr)
admin.site.register(Job_appl)
admin.site.register(Announcement)
