

Step 1: Install Django and required packages


bash
pip install django
pip install mysqlclient  # for MySQL database
# or pip install djongo  # for MongoDB database


Step 2: Create a new Django project


bash
django-admin startproject study_management


Step 3: Create a new Django app


bash
python (link unavailable) startapp study


Step 4: Configure (link unavailable)

In study_management/(link unavailable), add:



INSTALLED_APPS = [
    ...
    'study',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # or 'djongo'
        'NAME': 'study_management',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


Step 5: Define models

In study/models.py, add:



from django.db import models

class Sponsor(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Study(models.Model):
    study_id = models.AutoField(primary_key=True)
    study_name = models.CharField(max_length=255)
    study_description = models.TextField()
    study_phase = models.CharField(max_length=10, choices=[
        ('Phase I', 'Phase I'),
        ('Phase II', 'Phase II'),
        ('Phase III', 'Phase III'),
        ('Phase IV', 'Phase IV'),
    ])
    sponsor_name = models.ForeignKey(Sponsor, on_delete=models.CASCADE)

    def __str__(self):
        return self.study_name


Step 6: Create database tables


bash
python (link unavailable) makemigrations
python (link unavailable) migrate


Step 7: Create views

In study/views.py, add:



from django.shortcuts import render, redirect
from .models import Study, Sponsor
from .forms import StudyForm

def study_list(request):
    studies = Study.objects.all()
    return render(request, 'study/list.html', {'studies': studies})

def add_study(request):
    if request.method == 'POST':
        form = StudyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm()
    return render(request, 'study/add.html', {'form': form})

def view_study(request, pk):
    study = Study.objects.get(pk=pk)
    return render(request, 'study/view.html', {'study': study})

def edit_study(request, pk):
    study = Study.objects.get(pk=pk)
    if request.method == 'POST':
        form = StudyForm(request.POST, instance=study)
        if form.is_valid():
            form.save()
            return redirect('study_list')
    else:
        form = StudyForm(instance=study)
    return render(request, 'study/edit.html', {'form': form})

def delete_study(request, pk):
    study = Study.objects.get(pk=pk)
    study.delete()
    return redirect('study_list')


Step 8: Create templates

Create the following templates in study/templates/study/:


- list.html
- add.html
- view.html
- edit.html

Step 9: Create forms

In study/forms.py, add:



from django import forms
from .models import Study

class StudyForm(forms.ModelForm):
    class Meta:
        model = Study
        fields = ('study_name', 'study_description', 'study_phase', 'sponsor_name')


Step 10: Add URL patterns

In study/urls.py, add:



from django.urls import path
from . import views

urlpatterns = [
    path('', views.study_list, name='study_list'),
    path('add/', views.add_study, name='add_study'),
    path('view/<pk>/', views.view_study, name='view_study'),
    path('edit/<pk>/', views.edit_study, name='edit_study'),
    path('delete/<pk>/', views.delete_study, name='delete_study'),
]


Step 11: Run the application


bash
python (link unavailable) runserver


Open http://localhost:8000/ in your browser to access the application

To view - localhost:8000/study/
To add a new study - localhost:8000/study/add/
To delete a study - localhost:8000/study/delete/1/
To edit a study - localhost:8000/study/edit/1/
