from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')

def sign_in(request):
    return render(request, 'sign_in.html')  # Renders the Sign In page

def dashboard(request):
    return render(request, 'dashboard.html')  # Renders the Dashboard page

def add_client(request):
    return render(request, 'add_client.html')  # Renders the Add New Client page