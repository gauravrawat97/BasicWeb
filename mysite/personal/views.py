from django.shortcuts import render

def index(request):
    return render(request, 'personal/header.html')

def help(request):
    return render(request, 'personal/help.html',{'content':['Gaurav','Rawat','New','site']})