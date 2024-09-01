from django.urls import path
from .views import index, logout, login, add_user, update_user, delete_user, register

app_name = 'user'

urlpatterns = [
    path('users', index, name='index'),
    path('', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
    path('add/', add_user, name='add'),
    path('update/<int:user_id>/', update_user, name='update'),
    path('delete/<int:user_id>/', delete_user, name='delete'),
]
