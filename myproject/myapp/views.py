from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Topic,Webpage,AccessRecord
# Create your views here.

def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' :webpages_list}
    return render(request,'myapp/index.html',context=date_dict)

def help(request):
    helpdict = {'inserthelp':'Help page'}
    return render(request,'myapp/help.html',context=helpdict)
