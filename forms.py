from django import forms
from .models import Staff
# not needed
class Staff_form(forms.ModelForm):
	class meta:
		model=Blogpost
		fields= ['name','address', 'position', 'post']