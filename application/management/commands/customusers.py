from django.core.management import BaseCommand
from application.models import ApplicationUser, Student, Hr

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        admin = ApplicationUser.objects.create_superuser(
            username='admin',
            email='admin@admin.com',
            password='admin'
        )
        student = ApplicationUser.objects.create_superuser(
            username='student',
            email='student@student.com',
            password='student'
        )
        student.make_student(name='student')
        hr1 = ApplicationUser.objects.create_superuser(
            username='hr1',
            email='hr1@hr.com',
            password='hr1'
        )
        hr1.make_hr(name='hr1')
        hr2 = ApplicationUser.objects.create_superuser(
            username='hr2',
            email='hr2@hr.com',
            password='hr2'
        )
        hr2.make_hr(name='hr2')
        Company.objects.create(
            name='Company 1'
            email='company1@comp.com'
            description='Company 1'
        )
        Company.objects.create(
            name='Company 2'
            email='company2@comp.com'
            description='Company 2'
        )
