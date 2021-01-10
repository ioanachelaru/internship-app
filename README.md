# internship-app

## How to run
### Env setup
> virtualenv venv
> venv\Scripts\activate
(venv) > pip install -r requirements.txt

### Db, migrations stuff
(venv) > python manage.py makemigrations
// if no migrations are found
(venv) > python manage.py makemigrations application 
(venv) > python manage.py migrate --run-syncdb
(venv) > python manage.py createsuperuser
-> admin, student, hr
(venv) > python manage.py shell_plus
>>> ApplicationUser.objects.all() // show all users
>>> admin = ApplicationUser.objects.all()[0]
>>> student = ApplicationUser.objects.all()[1]
>>> student.make_student(name='student')
>>> hr = ApplicationUser.objects.all()[2]
>>> hr.make_hr(name='hr')
(venv) > python manage.py runserver