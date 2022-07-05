from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Members

# Create your views here.
def index(request):
    template = loader.get_template('myfirst.html')
    member_list = Members.objects.all().values()
    for x in member_list:
        print(x['firstname'])
    return HttpResponse(template.render())

def addrecord(request):
    x = request.POST['first']
    y = request.POST['last']
    new_member = Members(firstname = x, lastname = y)
    new_member.save()
    return HttpResponse(reverse('index'))

def delete(request, id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponse(reverse('index'))

def update(request, id):
    member = Members.objects.get(id=id)
    member.firstname = request.POST['first']
    member.lastname = request.POST['last']
    member.save()
    return HttpResponse(reverse('index'))