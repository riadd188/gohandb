# from datetime import date, timedelta
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from .models import Item
from django.utils import timezone
from datetime import datetime, timedelta, timezone


# Create your views here.
# from django.http import HttpResponse


# def index(request):
#     return render(request,"main.html")

class IndexView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        item_data = Item.objects.order_by("-id")
        for item in item_data:
            # print(type(datetime.now()))
            td = datetime.now(timezone(timedelta(hours=+9), 'JST')) - item.cleanup_date  
            if td.seconds < 2 :
                item.state = 1
            elif td.seconds < item.cycle * 0.5 :
                item.state = 2
            elif td.seconds < item.cycle :
                item.state = 3
            else :
                item.state = 4
            item.save()
        return render(request, "main.html", {
            "item_data" : item_data,
        })



class UpdateStateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        item_data = Item.objects.get(id=self.kwargs['pk'])
        item_data.cleanup_date = datetime.now(timezone(timedelta(hours=+9), 'JST'))
        item_data.save()
        return redirect('index')


