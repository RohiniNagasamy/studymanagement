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
