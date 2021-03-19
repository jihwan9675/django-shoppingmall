from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import RegisterForm
# from django.views.generic.edit import FormView
# Create your views here.


def index(request):
    return render(request, 'index.html')

class RegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/'