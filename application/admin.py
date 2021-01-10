from django.contrib import admin
from django.shortcuts import redirect
from application.models import Student, Company, Hr, JobApplication, Announcement


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_filter = ['name']

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    pass
    # def get_queryset(self, request):
    #     print(request)

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    
    actions = ['apply_to']

    def apply_to(self, request, queryset):
        print(request.user)
        print(queryset)
        announcement = queryset.first()
        application = JobApplication.object.create(
            student=request.user,
            announcement=announcement,
        )
        path = '/applications/${application.id}'
        return redirect(path)

    apply_to.short_description = 'Apply to announcements'
    apply_to.allowed_permissions = ['is_student']

    def has_is_student_permission(self, request):
        return hasattr(request.user, 'student')