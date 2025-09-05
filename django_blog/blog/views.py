from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CustomUserCreationForm, UserProfileForm

class CustomLoginView(LoginView):
    template_name = 'blog/login.html'
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('profile')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('home')

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        user = form.save()
        messages.success(self.request, 'Registration successful! Please log in.')
        return super().form_valid(form)

@login_required
def profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('profile')
    else:
        form = UserProfileForm(instance=request.user)
    
    return render(request, 'blog/profile.html', {'form': form})

def home_view(request):
    return render(request, 'blog/home.html')
