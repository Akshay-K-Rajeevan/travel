from django.shortcuts import render
from .models import Place, person


def demo(request):
    obj = Place.objects.all()
    obj1 = person.objects.all()
    return render(request,'index.html',{'result':obj,'res': obj1})
# Create your views here.
