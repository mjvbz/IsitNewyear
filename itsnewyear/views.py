from django.shortcuts import render

import datetime

# Create your views here.

now = datetime.datetime.now()

def index(request): 
  return render(request, 'newyear/index.html', {
    "isnewyear": now.month == '1' and now.day == '1'
  })
