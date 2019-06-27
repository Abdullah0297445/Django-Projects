from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from .models import Patient, DiagReport
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ReportCreateForm
from django.contrib.messages.views import SuccessMessageMixin


class ReportListView(ListView):
    
    model = DiagReport
    template_name = 'hospital_app/home.html'
    context_object_name = 'reports'
    ordering = ['-date_created']
    paginate_by = 5

class DocListView(ListView):
    
    model = User
    template_name = 'hospital_app/doc_view.html'
    context_object_name = 'docs'
    #ordering = ['-date_joined']
    paginate_by = 5
    
class PatListView(ListView):
    
    model = Patient
    template_name = 'hospital_app/pat_view.html'
    context_object_name = 'pats'
    #ordering = ['-date_joined']
    paginate_by = 5
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        
        
        return user.patient_set.all()
    
class DocReportListView(ListView):
    
    model = DiagReport
    template_name = 'hospital_app/doc_reports.html'
    context_object_name = 'docreps'
    paginate_by = 5    
    
    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        pat = user.patient_set.first()
        reports = pat.diagreport_set.all()
        for pat in user.patient_set.all():
            reports |= pat.diagreport_set.all()
        
        return reports.order_by('-date_created')#DiagReport.objects.filter(doc=user).order_by('-date_created')

class PatReportListView(ListView):
    
    model = Patient
    template_name = 'hospital_app/pat_reports.html'
    context_object_name = 'reports'
    paginate_by = 5    
    
    def get_queryset(self):
        
        pat = get_object_or_404(Patient, id=self.kwargs.get('pk'))
        reports = pat.diagreport_set.all()
        
        
        return reports.order_by('-date_created')
    
class ReportDetailView(DetailView):
    
    model = DiagReport
    
class ReportCreateView(LoginRequiredMixin, CreateView):
    
    model = DiagReport
    
    form_class = ReportCreateForm
    
    def form_valid(self, form):
        form.instance.pat.doc = self.request.user 
        return super().form_valid(form)

class ReportUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    
    model = DiagReport
    
    fields = ['title', 'rprt', 'pat']
    
    def form_valid(self, form):
        form.instance.pat.doc = self.request.user 
        return super().form_valid(form)

    def test_func(self):
        report = self.get_object()
        if self.request.user == report.pat.doc:
            return True
        else:
            return False

class ReportDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    
    model = DiagReport
    success_url = '/'
    def test_func(self):
        report = self.get_object()
        if self.request.user == report.pat.doc:
            return True
        else:
            return False
    
class PatientCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Patient
    success_message = 'New patient record has been added successfully !'
    fields = ['first', 'last', 'age', 'gender']
    template_name = 'hospital_app/patient_create.html'
    
    
    
    
    def form_valid(self, form):
        form.instance.doc = self.request.user 
        return super().form_valid(form)
    

class PatientUpdateView(LoginRequiredMixin,UserPassesTestMixin,  UpdateView):
    model = Patient
    
    fields = ['first', 'last', 'age', 'gender']
    template_name = 'hospital_app/patient_update.html'
    
#    def get_absolute_url(self):
#        return reverse('Pat-List', args=[self.request.user.username])
#    
    
    def form_valid(self, form):
        form.instance.doc = self.request.user 
        return super().form_valid(form)
    
    def test_func(self):
        patient = self.get_object()
        if self.request.user == patient.doc:
            return True
        else:
            return False

class PatientDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = Patient
    success_message = 'Patient record has been deleted!'
    template_name = 'hospital_app/patient_delete.html'

    def get_success_url(self):
        # I cannot access the 'pk' of the deleted object here
        return reverse('Pat-List', kwargs={'username':self.request.user.username})
    
    def test_func(self):
        patient = self.get_object()
        if self.request.user == patient.doc:
            return True
        else:
            return False

def about(request):
    return render(request, 'hospital_app/about.html', {"title":"About"})