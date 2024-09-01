from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .models import UserModel
from .forms import UserAddForm, UserRegisterForm


# Create your views here.
@login_required
def index(request):
    users = UserModel.objects.all()
    total = users.count()
    context = {'users': users, 'total': total}
    return render(request, 'users.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            messages.success(request, 'Inscription effectuée avec succès! Connectez-vous svp.')
            return redirect('user:login')
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        'title': 'Register',
    }

    return render(request, 'register.html', context)



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard:index')
        else:
            messages.error(request, 'Username ou mot de passe incorrect')

    return render(request, 'login.html')

@login_required
def add_user(request):
    if request.method == 'POST':
        form = UserAddForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('user:index')
        else:
            context = { 'form': form, 'title': 'Ajouter' }
    else:
        form = UserAddForm()
        context = {
            'form': form,
            'title': 'Modifier',
        }

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

@login_required
def delete_user(request, user_id):
    user = UserModel.objects.get(id=user_id)
    user.delete()
    return redirect('user:index')

def logout(request):
    auth_logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès.')
    return redirect('user:login')