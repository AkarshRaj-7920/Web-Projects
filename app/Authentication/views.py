from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.utils import timezone
from django.urls import reverse
from .models import PasswordReset
from app.crudpost.models import Post
from django.db import transaction

# Create your views here.
# def Home(request):
#     return render(request,'crudpost/home.html')

def RegisterView(request):

    if request.method == 'POST':
        #getting user input from frontend
        first_name = request.POST.get('first-name') 
        last_name = request.POST.get('last-name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        #initializing if user has error
        user_data_has_error = False

        if User.objects.filter(username = username).exists():
            user_data_has_error = True
            messages.error(request, 'Username already exists')

        if User.objects.filter(email = email).exists():
            user_data_has_error = True
            messages.error(request, 'Email already exists')

        if len(password) < 5:
            user_data_has_error = True
            messages.error(request, 'Password must be at least 5 characters lond')

        #if user does not has any error 
        if not user_data_has_error:
            try:
                with transaction.atomic():
                    new_user = User.objects.create_user(
                        first_name = first_name,
                        last_name = last_name,
                        username = username,
                        email = email,
                        password = password
                    )

                    email_body = f"Hi {first_name}!\nWondor welcomes you to our community thanks for joining"

                    email_message = EmailMessage(
                        subject = 'Welcome to Wondor!',
                        body= email_body,
                        from_email = settings.EMAIL_HOST_USER,
                        to = [email],
                    )

                    email_message.send(fail_silently = False)

                    messages.success(request, 'Account created successfully')
                    return redirect('Login')
            except Exception as e:
                print(f"Email Error: {e}")
                messages.error(request, f"Enter valid email address")
                return redirect('Register')

    return render(request,'Authentication/register.html')

    

def LoginView(request):

    # getting user data from frontend
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request = request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('Home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('Login')

    return render(request,'Authentication/login.html')

def LogoutView(request):

    logout(request)

    return redirect('Login')

def ForgotPassword(request):

    if request.method == 'POST':
        email = request.POST.get('email')

        try:
            user = User.objects.get(email = email)

            #Create new reset_id
            new_password_reset = PasswordReset(user = user)
            new_password_reset.save()

            #Create password reset url
            password_reset_url = reverse('reset-password', kwargs = {'reset_id': new_password_reset.reset_id})

            full_password_rest_url = f'{request.scheme}://{request.get_host()}{password_reset_url}'

            #Email_content
            email_body = f'Reset your password using the link below:\n\n\n{full_password_rest_url}'

            email_message = EmailMessage(
                'Reset your password',
                email_body,
                settings.EMAIL_HOST_USER,
                [email]
            )

            email_message.fail_silently = True
            email_message.send()

            return redirect('password-reset-sent', reset_id = new_password_reset.reset_id)

        except User.DoesNotExist:
            messages.error(request, f'No user with email \'{email}\' found')
            return redirect('forgot-password')

    return render(request, 'Authentication/forgot_password.html')
 
def PasswordResetSent(request, reset_id):

    if PasswordReset.objects.filter(reset_id = reset_id).exists():
        return render(request, 'Authentication/password_reset_sent.html')

    else:
        messages.error(request, 'Invalid reset id')
        return redirect('forgot-password')
    
def ResetPassword(request, reset_id):

    try:
        password_reset_id = PasswordReset.objects.get(reset_id = reset_id)

        if request.method == 'POST':
            password = request.POST.get('password')
            confirm_password = request.POST.get('confirm_password')

            password_have_error = False

            if password != confirm_password:
                password_have_error = True
                messages.error(request, 'Password do not match')

            if len(password) < 5:
                password_have_error = True
                messages.error(request, 'Password must be atleast 5 characters long')

            expiration_time = password_reset_id.created_when + timezone.timedelta(minutes=10)

            if timezone.now() > expiration_time:
                password_have_error = True
                messages.error(request, 'Reset link has expired')

                password_reset_id.delete()

            if not password_have_error:
                user = password_reset_id.user
                user.set_password(password)
                user.save()

                password_reset_id.delete()

                messages.success(request, 'Password reset. Proceed to login')
                return redirect('Login')

            else:
                return redirect('reset-password', reset_id = reset_id)

    except PasswordReset.DoesNotExist:

        messages.error(request, 'Invalid reset Id')
        return redirect('forgot-password')

    return render(request, 'Authentication/reset_password.html')


@login_required
def ProfileView(request, username):
    user_to_view = get_object_or_404(User, username = username)

    user_posts = Post.objects.filter(author = user_to_view).order_by('-created_at')

    context = {
        'user_profile': user_to_view,
        'posts': user_posts,
    }

    return render(request, 'Authentication/profile.html', context)

    