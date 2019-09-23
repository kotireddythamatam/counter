from django.shortcuts import render
from .models import Login
from django.http import HttpResponse
# Create your views here.

def login(request):
    if request.method == "GET":
        return render(request,'login.html')
    elif request.method == "POST":
        user = request.POST['username']
        password = request.POST['password']
        try:
            obj = Login.objects.get(Username=user,Password=password)
            count = obj.Counter
            if obj:
                count += 1
                obj.Counter=count
                obj.save()
        except:
                count = 1
                obj = Login(Username=user,Password=password,Counter=count)
                obj.save()
        model_obj = Login.objects.all()
        return render(request,'display.html',{'model_obj':model_obj})
