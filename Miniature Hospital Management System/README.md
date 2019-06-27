# Miniature Hospital Management System

### It is a simple web application writen in Django Framework. It involves 3 entities (models):

1. Doctors
2. Patients (One doctor can have multiple patients but a single patient can't have multiple doctors)
3. DiagnosisReports (One patient can have multiple reports from a same doctor)

### Some of the basic functionalities include:

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

### To get this project running:

1. Make sure you have python compiler or anaconda distribution of python installed in your pc. 
2. If you have installed native python compiler then make sure it is added into your environment variable.
3. Clone this project/repository.
4. ```cd``` into 'Miniature Hospital Management System' directory.
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

To access the admin page of this application, type:
```
localhost:8000/admin/
```

Feel free to experiment with it. </br> This app is actually tested on Windows 10 on Anaconda Python 3.6.3. Django version 2.2 

### Improvements

1. There is currently one flaw in this application - When a registered doctor tries to add a new diagnosis report he must select a patient from the dropdown list. Naturally that dropdown list should only show patients which are under treatment of this doctor only. But what is happening here is that the drop down list shows the patients which are under treatment of other doctors too. So, if this doctor chooses a patient which is not under his treatment and saves the report. It actually gets saved under the orignal doctor of that patient. 
2. A search functionality should be added to this application. You can be able to search a doctor, a patient or a diagnosis report. 


