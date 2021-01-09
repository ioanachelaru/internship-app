# internship-app

* to install dependencies: 
\internship-app> pip install -r requirements.txt

python manage.py shell_plus
ApplicationUser.objects.first()

admin.is_superuser = False
admin.save()
admin.user_permissions.add(Permission.objects.get(codename='view_announcement'))
>>> Permission.objects.all()
<QuerySet [<Permission: admin | log entry | Can add log entry>, <Permission: admin | log entry | Can change log entry>, <Permission: admin | log entry | Can delete log entry>, <Permission: admin | log entry | Can view log entry>, <Permission: application | announcement | Can add announcement>, <Permission: application | announcement | Can change announcement>, <Permission: application | announcement | Can delete announcement>, <Permission: application | announcement | Can view announcement>, <Permission: application | company | Can add company>, <Permission: application | company | Can change company>, <Permission: application | company | Can delete company>, <Permission: application | company | Can view company>, <Permission: application | hr | Can add hr>, <Permission: application | hr | Can change hr>, <Permission: application | hr | Can delete hr>, <Permission: application | hr | Can view hr>, <Permission: application | job application | Can add job application>, <Permission: application | job application | Can change job application>, <Permission: application | job application | Can delete job application>, <Permission: application | job application | Can view job application>, '...(remaining elements truncated)...']>
['add_announcement', 'change_announcement', 'delete_announcement', 'view_announcement']

