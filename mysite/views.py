from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from .models import subs
from .models import film
from .models import memory
from .models import person
import os
from django.utils.datastructures import MultiValueDictKeyError
from django import forms

# (eb-virt) xiemindeMacBook-Pro:ebdjango craig$ source ~/eb-virt/bin/activate
# Create your views here.

def index(request):
    return render(request, 'mysite/index.html')


def members(request):
    if request.method == "POST":
        email = request.POST.get('email')
        newsub = subs(email=email)
        newsub.save()
        return render(request, 'mysite/thank.html')
    else:
        return render(request, 'mysite/members.html')


def shorts(request):
    all_films = film.objects.all()
    return render(request, 'mysite/shorts.html',{"films": all_films})


def activities(request):
    all_memories = memory.objects.all()
    if request.method == "POST":
        try:
            image = request.FILES['image']
        except MultiValueDictKeyError:
            return render(request, 'mysite/activities.html', {"memories": all_memories})

        extension = image.name.split('.')[-1]
        if extension not in ['jpg', 'jpeg', 'png']:
            return HttpResponseRedirect("/activities")
        name = request.POST.get('title')
        user = request.POST.get('user')
        password = request.POST.get('password')
        try:
            uploader = person.objects.get(name=user)
        except person.DoesNotExist:
            return render(request, 'mysite/usernotfounderror.html')
        if password != uploader.password:
            return render(request, 'mysite/passwordwrong.html')

        mem = memory(pic=image, name=name, uploaded_by=user)
        mem.save()
        return HttpResponseRedirect("/activities")
    else:
        return render(request, 'mysite/activities.html', {"memories": all_memories})

