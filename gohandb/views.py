# from datetime import date, timedelta
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.utils import timezone
from datetime import datetime, timedelta, timezone

from django.views.generic import TemplateView
 
class IndexTemplateView(TemplateView):
    template_name = "main.html"

# Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return render(request,"main.html")

# class LoginView(views.LoginView):
#     template_name = 'login.html'

# class IndexView(views.IndexView):
#     template_name = 'main.html'
