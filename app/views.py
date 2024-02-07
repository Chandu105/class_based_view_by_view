from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *
# Create your views here.

#returning string as a response by function based view
def fbv_string(request):
    return HttpResponse('THIS IS FUNCTION BASED VIEW BY IN STRINGS')

#returning string as a response by class based view
class cbv_string(View):
    def get(self,request):
        return HttpResponse('this is string by class based view')
    
#rendering html by function based view
    
def fbvhtml(request):
    return render(request,'fbvhtml.html')
    
#rendering html by class based view
class cbvhtml(View):
    def get(self,request):
        return render(request,'cbvhtml.html')
    
#insert data by functon based view through model forms
    
def insert_school_by_fbv(request):
    SFO=SchoolForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert school by fbv is done')
    return render(request,'insert_school_by_fbv.html',d)

#insert  data by class based view through model forms

class insert_school_by_cbv(View):
    def get(self,request):
        ESFO=SchoolForm()
        d={'ESFO':ESFO}
        return render(request,'insert_school_by_cbv.html',d)
    
    def post(self,request):
        SFDO=SchoolForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_school_by_cbv is done')
        

class cbv_Template(TemplateView):
    template_name='cbv_Template.html'
        


    


