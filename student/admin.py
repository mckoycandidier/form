# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Details, Course, Subject, professor

#@admin.register(Details)
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ("course_name", "description", )
	list_editable = ("description",)
	list_filter = ("course_name", )
	search_fields = ("course_name",  )

admin.site.register(Details)
#admin.site.register(Course, CourseAdmin)
admin.site.register(Subject)
#admin.site.register(professor)

# Register your models here.
