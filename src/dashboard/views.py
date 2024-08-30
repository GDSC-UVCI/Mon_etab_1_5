from django.shortcuts import render

from student.models import StudentModel
from teacher.models import TeacherModel
from user.models import UserModel



# Create your views here.
def index(request):
    students = StudentModel.objects.all().count()
    users = UserModel.objects.all().count()
    teachers = TeacherModel.objects.all().count()
    context = {
        'students': students,
        'users': students,
        'teachers': teachers
    }
    return render(request, 'dashboard.html', context)