from django import forms
from .models import Details

class StudentForm(forms.ModelForm):
	class Meta:
		model = Details
		fields = ['first_name',
		'last_name',
		'middle_name',
		'age',
		'birthday',
		'course']
