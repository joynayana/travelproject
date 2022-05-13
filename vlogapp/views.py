from django.shortcuts import render
from . models import current

# Create your views here.
def vlog(request):
    obj1=current.objects.all()
    #this function only created for importing view to travelapp views
    return ;