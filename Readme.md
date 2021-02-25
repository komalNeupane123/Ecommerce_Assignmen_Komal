Project Summary: At first, I initialized Django project: django-admin startproject ecom_lab_exam. 
After that I ensured that the required database and tables are initialized correctly by using folling code : python manage.py migrate python manage.py createsuperuser
Then, I added a module using code: python manage.py startapp ecommerce. It was registered to ‘INSTALLED APPS’ @settings.py. 
Then I added model LabExam inside module: 
class LabExam(models.Model): 
exam_date = models.DateTimeField()
exam_name = models.CharField(max_length=20) 
exam_description = models.CharField(max_length=500) 
total_marks = models.FloatField()
pass_marks = models.FloatField() 
exam_status = models.BooleanField() 
The created table shall be migrated into the database. 
Then the model is registered into @admin.py: admin.site.register(LabExam) CRUD operation was performed after running the server.
** The database is handled in the following section of project @settings.py: DATABASES = 
{ 'default': { 'ENGINE': 'django.db.backends.sqlite3', 'NAME': BASE_DIR / 'db.sqlite3', } }

Features of My Project: I have created sqlite database. Admin can perform different operation including Create,Delete,Read inside a database.
