from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SignUpForm

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(
                request,
                f'Account created for {user.username}! You can now log in.'
            )
            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'users/register.html', {'form': form})
