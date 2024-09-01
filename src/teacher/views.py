from django.shortcuts import render, redirect
from .models import TeacherModel
from .forms import TeacherAddForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
    teachers = TeacherModel.objects.all()
    total = teachers.count()
    context = {'teachers': teachers, 'total': total}
    return render(request, 'teachers.html', context)

@login_required
def add_teacher(request):
    context = {}
    if request.method == 'POST':
        form = TeacherAddForm(request.POST)
        if form.is_valid():
            form.save()
            context['form'] = form
            return redirect('teacher:index')
        else:
            context['form'] = form
    else:
        form = TeacherAddForm()
        context['form'] = form
        context['title'] = 'Ajouter'

    return render(request, 'add_teacher.html', context)

@login_required
def update_teacher(request, teacher_id):
    teacher = TeacherModel.objects.get(id=teacher_id)
    context = {}
    if request.method == 'POST':
        form = TeacherAddForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher:index')
        else:
            context['form'] = form
    else:
        form = TeacherAddForm(instance=teacher)
        context['form'] = form
        context['title'] = 'Modifier'

    return render(request, 'add_teacher.html', context)


@login_required
def delete_teacher(request, teacher_id):
    teacher = TeacherModel.objects.get(id=teacher_id)
    teacher.delete()
    return redirect('teacher:index')