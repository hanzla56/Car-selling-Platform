from django.shortcuts import render , redirect # import manually
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm , UserChangeForm
from django.contrib.auth import login , logout

# Create your views here.
def register(request):
    if request.method == 'POST':
        reg_form = UserCreationForm(request.POST)
        if reg_form.is_valid():
            reg_form.save()
            return redirect('accounts:login')

    else:
        reg_form = UserCreationForm()

    return render(request , 'accounts/register.html' , {'reg_form' : reg_form})       



def login_view(request):
    if request.method == 'POST':
      log_form = AuthenticationForm(data = request.POST)
      if log_form.is_valid():
          user = log_form.get_user()
          login(request , user)
          return redirect('Car_Platform:home_page')
    
    else:
        log_form = AuthenticationForm()

    return render(request , 'accounts/login.html' , {'log_form' : log_form})     



def logout_view(request):
    logout(request)
    return redirect('accounts:login')
