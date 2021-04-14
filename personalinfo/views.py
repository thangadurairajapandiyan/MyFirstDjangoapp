from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import Personal, Color


def home(request):
    # return HttpResponse("test")
    return render(request, 'home.html')


def about(request):
    # return HttpResponse("test")
    return render(request, 'about.html')


def contact(request):
    # return HttpResponse("test")
    return render(request, 'contact.html')


def skill(request):
    # return HttpResponse("test")
    sk = Personal.objects.all()
    output = {
        'Personal': sk
    }
    return render(request, 'Skills.html', output)


def save_value_to_model(request):
    if request.method == 'POST':
        if request.POST.get('clr'):
            savevalue = Color()
            savevalue.clr = request.POST.get("clr")
            savevalue.save()
            messages.success(request,"successfully saved color into data base")
            return render(request, 'Skills.html')
    else:
        return render(request, 'Skills.html')
