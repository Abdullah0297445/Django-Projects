# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from .models import DiagReport


class ReportCreateForm(forms.ModelForm):
    
    class Meta:
        
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['pat'].queryset = User.patient_set.filter(username=self.user.username)
            
        model = DiagReport
        fields = ['pat' ,'title', 'rprt', ]
        
        