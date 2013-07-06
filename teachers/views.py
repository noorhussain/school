# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from teachers.models import Details
from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic.base import TemplateView
from teachers.forms import *

class Add(TemplateView):
    template_view='add.html'
    def get(self,request):
         form=TestForm()
         return render_to_response('add.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
         form=TestForm(request.POST)
         if form.is_valid():
             name = form.cleaned_data['faculty_name']
             age=form.cleaned_data['faculty_age']
             main_sub=form.cleaned_data['main_subject']
             uid=form.cleaned_data['faculty_Idn']
             salary = form.cleaned_data['salary']
             Details.objects.create(faculty_name=name,faculty_age=age,main_subject=main_sub,faculty_Idn=uid,salary=salary)
             HttpResponseRedirect('/teachers/')
         else:
             return HttpResponseRedirect('/error/')
             #return HttpResponse('Some Problem')
         return HttpResponseRedirect('/teachers/')

class Detail(TemplateView):
    template_view='detail.html'
    def get(self, request):
        s=Details.objects.all()
        return render_to_response('detail.html',locals(),context_instance=RequestContext(request))

class Show(TemplateView):
    template_view='show.html'
    def get(self,request,id):
        s=Details.objects.get(id=id)
        return render_to_response('show.html',locals(),context_instance=RequestContext(request))

class Delete(TemplateView):
    def get(self,request,id):
        d=Details.objects.get(id=id)
        d.delete()
        return render(request,'detail.html')
class Error(TemplateView):
    def get(self,request):
        return render(request,'error.html')
