from django.shortcuts import render, redirect
from .forms import NewCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.http import HttpResponse
def register_user(request):
    form = NewCreationForm()
    if request.method == 'POST':
        form = NewCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registratsion successful.")
            return redirect('index')
        messages.error(request, "Unsuccessful registratsion. Invalid informatsion.")

    return render(request, "auth/register.html", {'form': form})

def login_user(request):
    form = AuthenticationForm()
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("index")
            else:
                messages.error(request, "Invalid username or password." )
        else:
           messages.error(request, "Form is not valid.")
    return render(request, "auth/login.html", {"form": form})
def logout_user(reauest):
    logout(reauest)
    messages.info(reauest, "User logged out!")
    return redirect('index')

# Create your views here.
def user_password_reset(request):
    form = PasswordResetForm()
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            users = User.objects.filter(email=email)
            subject = "Password Reset Requested"
            email_template_name = "auth/password_reset_email.txt"
            if users.exists():
                for user in users:
                    subject = "Password Reset Requeested"
                    email_template_name = "auth/password_reset_email.txt"
                    data = {
                        "email": user.email,
                        "domain": "127.0.0.1:8000",
                        "site_name": "Online Website",
                        "user": user,
                        "protocol": "http",
                        "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                        "token": default_token_generator.make_token(user)
                    }
                    email_message = render_to_string(email_template_name, data)
                    try:
                        send_mail(
                            subject=subject,
                            message=email_message,
                            from_email='sardoryuldashov9999@gmail.com',
                            recipient_list=[user.email],
                            fail_silently=False
                        )
                    except BadHeaderError:
                        return HttpResponse('Invalid header found.')
                    return redirect('password_reset_done')
        return render(request, "auth/password_reset.html", {"form": form})
