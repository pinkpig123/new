from django.shortcuts import render, HttpResponse
from django.db.models import signals
from app01.models import User
# Create your views here.


def xxx(*args, **kwargs):
    print("111")
signals.pre_save.connect(xxx)

def login(request):
    User.objects.create(name="wr", password="123", age=18)
    return HttpResponse("HELLO")
