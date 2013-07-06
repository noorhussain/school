# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from staff.models import detail
from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic.base import TemplateView
from staff.forms import *

class Addst(TemplateView):
    template_view='addst.html'
    def get(self,request):
         form=TestForm()
         return render_to_response('addst.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
         form=TestForm(request.POST)
         if form.is_valid():
             name = form.cleaned_data['staff_name']
             age=form.cleaned_data['staff_age']
             section=form.cleaned_data['section']
             uid=form.cleaned_data['staff_Idn']
             salary = form.cleaned_data['salary']
             detail.objects.create(staff_name=name,staff_age=age,section=section,staff_Idn=uid,salary=salary)
             HttpResponseRedirect('/staff/')
         else:
             return HttpResponseRedirect('/error/')
             #return HttpResponse('Some Problem')
         return HttpResponseRedirect('/staff/')

class Detailst(TemplateView):
    template_view='detailst.html'
    def get(self, request):
        s=detail.objects.all()
        return render_to_response('detailst.html',locals(),context_instance=RequestContext(request))

class Showst(TemplateView):
    template_view='showst.html'
    def get(self,request,id):
        s=detail.objects.get(id=id)
        return render_to_response('showst.html',locals(),context_instance=RequestContext(request))

class Deletest(TemplateView):
    def get(self,request,id):
        d=detail.objects.get(id=id)
        d.delete()
        return render(request,'detailst.html')
class Errorst(TemplateView):
    def get(self,request):
        return render(request,'errorst.html')
