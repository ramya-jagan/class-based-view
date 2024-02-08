from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *


# Create your views here.

def fbv_string(request):
  return HttpResponse('this is fbv string')

class cbv_string(View):
  def get(self,request):
    return HttpResponse('this is class based view string')


def fbv_html(request) :
  return render(request,'fbvhtml.html') 

class cbv_html(View):
  def get(self,request):
    return render(request,'cbvhtml.html')   

def fbv_form(request):
    sfo=SchoolForm()
    d={'sfo':sfo}

    if request.method=='POST':
      sfbo=SchoolForm(request.POST)
      if sfbo.is_valid():
        sfbo.save()
        return HttpResponse('insert_school_by_fbv is done')
    return render(request,'fbvform.html',d)


class InsertSchoolByCbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'InsertSchoolByCbv.html',d)
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('InsertSchoolByCbv is done')

class cbv_template(TemplateView):
     template_name='cbv_template.html'           
   
    


