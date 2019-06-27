#**Miniature Hospital Management System**

It is a simple web application writen in Django Framework. It involves 3 entities (models):

- Doctors
- Patients (One doctor can have multiple patients but a single patient can't have multiple doctors)
- DiagnosisReports (One patient can have multiple reports from a same doctor)

Some of the basic functionalities include:

- Main page is just like a feed where all the Diagnosis reports of all the doctors appear sorted by the latest report by any doctor.
- You can create a New Doctor via 'Register' Link on the main page.
- After creating a New Doctor profile you can login to the app as that registered doctor.
- After logging in a doctor can add multiple patients.
- After adding patients doctor can add multiple diagnosis reports for each patient. 
- Similarly doctor can delete or modify all it patients' records but not the patients of other doctors.
- Doctor can also delete or modify individual reports of any particular patient. 
- Doctor can see a list of all his/her patients.
- Doctor can see a list of all his Diagnosis Reports for all the patients.
- Upon deletion of a patient all the Diagnosis reports related to that patient will be deleted too. 
- Upon deletion of a doctor all the Patients and all their respective Diagnosis reports will be deleted too. 
- and more.

###To get this project running:

1. Make sure you have python compiler or anaconda distribution of python installed in your pc. 
2. If you have python installed then make sure it is added into your environment variable.
3. Clone this project/repository.
4. ```cd``` into 'Miniature Hospital Management System' dicrectory.
5. run command in cmd(if you have native python) or anaconda prompt(if you have anaconda):

```python
python manage.py runserver
```

You'll get a response similar to this:

```
C:\Users\abdul\Desktop\django_project>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
June 27, 2019 - 13:22:47
Django version 2.2.2, using settings 'django_project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

After getting this head to your chrome browser and type:
```
localhost:8000/
```
