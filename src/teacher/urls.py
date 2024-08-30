from django.urls import path
from .views import index, add_teacher, update_teacher, delete_teacher

app_name = 'teacher'

urlpatterns = [
    path('', index, name='index'),
    path('add/', add_teacher, name='add'),
    path('update/<int:teacher_id>/', update_teacher, name='update'),
    path('delete/<int:teacher_id>/', delete_teacher, name='delete'),
]
