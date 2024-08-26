from django.urls import path
from .views import index, login

app_name = 'user'

urlpatterns = [
    path('users', index, name='index'),
    path('', login, name='login'),
]
