from django.http import HttpResponse,HttpResponseRedirect
from students.models import details
from django.shortcuts import render,render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from django.views.generic.base import TemplateView
from students.forms import *

class Adds(TemplateView):
    template_view='adds.html'
    def get(self,request):
         form=TestForm()
         return render_to_response('adds.html',locals(),context_instance=RequestContext(request))
    def post(self, request):
        form=TestForm(request.POST)
        if form.is_valid():
             student = form.cleaned_data['Student_name']
             class_ = form.cleaned_data['student_class']
             main_sub=form.cleaned_data['main_subjects']
             Id=form.cleaned_data['student_Id_no']
             marks=form.cleaned_data['marks_student']
             Average=form.cleaned_data['Average_marks']
             Fee=form.cleaned_data['Fee_student']
             details.objects.create(Student_name=student,student_class=class_,main_subjects=main_sub,
                                   student_Id_no=Id,marks_student=marks,Average_marks=Average,Fee_student=Fee)
             HttpResponseRedirect('/students/')
        else:
             return HttpResponseRedirect('/errors/')
             #return HttpResponse('Some Problem')
        return HttpResponseRedirect('/students/')

class Details(TemplateView):
    template_view='details.html'
    def get(self, request):
        s=details.objects.all()
        return render_to_response('details.html',locals(),context_instance=RequestContext(request))

class Shows(TemplateView):
    template_view='shows.html'
    def get(self,request,id):
        s=details.objects.get(id=id)
        return render_to_response('shows.html',locals(),context_instance=RequestContext(request))

class Deletes(TemplateView):
    def get(self,request,id):
        d=details.objects.get(id=id)
        d.delete()
        return render(request,'details.html')
class Errors(TemplateView):
    def get(self,request):
        return render(request,'errors.html')
class school(TemplateView):
    def get(self,request):
        return render(request,'school.html')
