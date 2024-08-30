from .models import StudentModel
from django.shortcuts import render, redirect, get_object_or_404
from .forms import StudentAddForm

def index(request):
    students = StudentModel.objects.all()
    context = {'students': students}
    return render(request, 'students.html', context)

def add_student(request):
    context = {}
    if request.method == 'POST':
        form = StudentAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student:index')
        else:
            context['form'] = form
    else:
        form = StudentAddForm()
        context['form'] = form
        context['title'] = 'Ajouter'

    return render(request, 'add_student.html', context)

def update_student(request, student_id):
    student = get_object_or_404(StudentModel, id=student_id)
    context = {}
    if request.method == 'POST':
        form = StudentAddForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student:index')
        else:
            context['form'] = form
    else:
        form = StudentAddForm(instance=student)
        context['form'] = form
        context['title'] = 'Modifier'

    return render(request, 'add_student.html', context)



def delete_student(request, student_id):
    student = get_object_or_404(StudentModel, id=student_id)
    student.delete()
    return redirect('student:index')