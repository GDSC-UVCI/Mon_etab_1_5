from django.urls import path
from .views import index, add_student, update_student, delete_student

app_name = 'student'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_student, name='add'),
    path('update/<int:student_id>/', update_student, name='update'),
    path('delete/<int:student_id>/', delete_student, name='delete'),
]
