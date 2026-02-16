from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .models import CustomUser
from .forms import CustomUserCreationForm

# Professional helper: Ensures only Super Admins can manage users
def is_superuser(user):
    return user.is_authenticated and user.is_superuser

def home(request):
    return render(request, 'accounts/home.html')

@login_required
@user_passes_test(is_superuser)
def user_list(request):
    # Fetching all documents from MongoDB
    users = CustomUser.objects.all()
    return render(request, 'accounts/user_list.html', {'users': users})

@login_required
@user_passes_test(is_superuser)
def user_create(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "User document created successfully.")
            return redirect('user_list')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/user_form.html', {'form': form})

# NEW: Update function (Fixes the AttributeError)
@login_required
@user_passes_test(is_superuser)
def user_update(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.info(request, f"User {user.email} updated successfully.")
            return redirect('user_list')
    else:
        form = CustomUserCreationForm(instance=user)
    return render(request, 'accounts/user_form.html', {'form': form})

# NEW: Delete function
@login_required
@user_passes_test(is_superuser)
def user_delete(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    if request.method == 'POST':
        email = user.email
        user.delete()
        messages.warning(request, f"User {email} has been removed.")
        return redirect('user_list')
    return render(request, 'accounts/user_confirm_delete.html', {'user': user})