from lib2to3.fixes.fix_input import context

from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserAddForm

# Create your views here.
def index(request):
    users = UserModel.objects.all()
    total = users.count()
    context = {'users': users, 'total': total}
    return render(request, 'users.html', context)

def login(request):
    return render(request, 'login.html')

def add_user(request):
    context = {}
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()
            context['form'] = form
            return redirect('user:index')
        else:
            context['form'] = form
    else:
        form = UserAddForm()
        context['form'] = form
        context['title'] = 'Ajouter'

    return render(request, 'add_user.html', context)


def update_user(request, user_id):
    user = UserModel.objects.get(id=user_id)  # Retrieve the user instance
    if request.method == 'POST':
        form = UserAddForm(request.POST, instance=user)  # Pass the user instance to the form
        if form.is_valid():
            form.save()  # Save updates to the existing user
            return redirect('user:index')  # Redirect after successful update
    else:
        form = UserAddForm(instance=user)  # Initialize form with the user instance

    context = {
        'form': form,
        'title': 'Modifier',
    }

    return render(request, 'add_user.html', context)  # Render the template with the form and context


def delete_user(request, user_id):
    user = UserModel.objects.get(id=user_id)
    user.delete()
    return redirect('user:index')