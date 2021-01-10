from django.contrib import admin
from django.shortcuts import redirect
from application.models import Student, Company, Hr, JobApplication, Announcement


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_filter = ['name']

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    def get_queryset(self, request):
        qs = super(JobApplicationAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs
        print(qs)
        return qs.filter(student=Student.objects.filter(username=request.user).first())

    def add_view(self, request, object_id, extra_context=None):       
        self.exclude = ('status', )
        return super(JobApplicationAdmin, self).change_view(request, object_id, extra_context)

    def delete_view(self, request, object_id, extra_context=None):       
        self.exclude = ('status', )
        return super(JobApplicationAdmin, self).change_view(request, object_id, extra_context)

    # list_display = ['attachments']
    # readonly_fields = ('announcement',)
    # def get_queryset(self, request):
    #     print(request)

    # def announcement(self):
    #     print('announcement', instance)
    #     return mark_safe("<span class='errors'>I can't determine this address.</span>")

    # # short_description functions like a model field's verbose_name
    # announcement.short_description = 'Announcement field'

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    actions = ['apply_to']

    def apply_to(self, request, queryset):
        print(request.user)
        print(queryset)
        student=Student.objects.filter(username=request.user).first()
        announcement = queryset.first()
        # application = JobApplication.objects.create(
        #     student=Student.objects.filter(name=request.user).first(),
        #     announcement=announcement,
        # )
        path = f'/admin/application/jobapplication/add/?announcement={announcement.id_ann}&student={student.id}'
        return redirect(path)

    apply_to.short_description = 'Apply to announcements'
    apply_to.allowed_permissions = ['is_student']

    def has_is_student_permission(self, request):
        return hasattr(request.user, 'student')