from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Patient(models.Model):
    
    MALE = 'M'
    FEMALE = 'F'
    GENDER = [(MALE,'Male'),(FEMALE, 'Female')]
    
    doc = models.ForeignKey(User, on_delete=models.CASCADE)
    first = models.CharField(max_length = 50)
    last = models.CharField(max_length = 50, blank=True)
    age = models.PositiveIntegerField(validators=[MaxValueValidator(80), MinValueValidator(1)])
    gender = models.CharField(max_length = 1, choices=GENDER)
    
    def __str__(self):
        return str(self.first) + " " + str(self.last)
    
    def get_absolute_url(self):
        return reverse('Pat-List', kwargs={'username':self.doc.username})#return reverse('Hospital-Home')
    

class DiagReport(models.Model):
    
    pat = models.ForeignKey(Patient, on_delete=models.CASCADE)
    title = models.CharField(max_length = 100)
    date_created = models.DateTimeField(default=timezone.now)
    rprt = models.TextField()
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('report-detail', kwargs = {'pk': self.pk})
  
        
