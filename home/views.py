from django.urls import path
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.models import User
from .models import ContactMessage, FinancialData
from django.http import JsonResponse

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


# Check if the user is a superuser
def is_superuser(user):
    return user.is_superuser

# Admin Page View
@user_passes_test(is_superuser)
def admin(request):
    users = User.objects.all()  # Fetch all users
    return render(request, 'admin.html', {'users': users})

# Messages Page View
@user_passes_test(is_superuser)
def messages(request):
    # Example: Fetch messages from a database model (if implemented)
    messages = []  # Replace with actual query if messages are stored
    return render(request, 'messages.html', {'messages': messages})

# Home Page View
def home(request):
    return render(request, 'home.html')

# About Page View
def about(request):
    return render(request, 'about.html')

# Contact Page View
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        ContactMessage.objects.create(name=name, email=email, message=message)
        return render(request, 'contact.html', {'success': True})
    return render(request, 'contact.html')

# Login Page View
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        # Authenticate user using email
        try:
            username = User.objects.get(email=email).username  # Get username from email
        except User.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            # Redirect superuser to admin page, others to user page
            if user.is_superuser:
                return redirect('admin')  # Redirect to admin page
            else:
                return redirect('user_page')  # Redirect to user page
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')

# Signup Page View
def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            return render(request, 'signup.html', {'error': 'Username already exists'})
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        auth_login(request, user)  # Automatically log in the user after signup
        return redirect('user_page')  # Redirect to user page after signup
    return render(request, 'signup.html')

# User Page View
def user_page(request):
    if not request.user.is_authenticated:
        return redirect('login')

    # Get or create the user's financial data
    financial_data, created = FinancialData.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        if 'income' in request.POST:  # Adding income
            income = float(request.POST.get('income'))
            financial_data.monthly_income += income
            financial_data.incomes["Salary"] = financial_data.incomes.get("Salary", 0) + income
            financial_data.save()
        elif 'amount' in request.POST:  # Adding spending
            amount = float(request.POST.get('amount'))
            category = request.POST.get('category')
            financial_data.expenses[category] = financial_data.expenses.get(category, 0) + amount
            financial_data.monthly_spending += amount
            financial_data.monthly_income -= amount
            financial_data.save()

        # Return JSON response for AJAX
        return JsonResponse({
            'monthly_income': financial_data.monthly_income,
            'monthly_spending': financial_data.monthly_spending,
            'expenses': financial_data.expenses,
            'incomes': financial_data.incomes,
        })

    return render(request, 'user.html', {
        'username': request.user.username,
        'monthly_income': financial_data.monthly_income if financial_data.monthly_income > 0 else None,
        'monthly_spending': financial_data.monthly_spending if financial_data.monthly_spending > 0 else None,
        'expenses': financial_data.expenses,
        'incomes': financial_data.incomes,
    })

# Logout View
def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to home page after logout

