# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, redirect, render

from django.views.generic import DetailView, View
from .forms import StudentForm
from .models import Course, Details
# Create your views here.

def list_student(request):
	students = Details.objects.exclude()
	context = {
		'students': students
	}
	return render(request, "index.html", context)
	
class CourseList(View):
	def get(self, request):
		courses = Course.objects.all()
		context = {
			'courses': courses,
		}
		return render(request, "course.html", context)

class StudentDetail(DetailView):
	model = Details
	template_name = "students.html"
	
	def get_context_data(self, **kwargs):
		context = super(StudentDetail, self).get_context_data(**kwargs)
		return context
		
	
class CourseDetail(DetailView):
	model = Course
	template_name = "course-details.html"
	
	def get_context_data(self, **kwargs):
	
		context = super(CourseDetail, self).get_context_data(**kwargs)
		return context
	

class Student(View):
	def get(self, request):
		student = Details.objects.all()
		context = {
			'student' : student,
			'form' : StudentForm,
		}
		return render(request, "student-form.html", context)
	
	def post(self, request):
		form = StudentForm(request.POST)
		student = Details.objects.all()
		
		if form.is_valid():
			form.save()
			return redirect('student')
			
		context = {
			'form' : form,
			'student' : student,
		}
		
		return render(request, "student-form.html", context)
		