from django import forms

class NameForm(forms.Form):
	your_name = forms.CharField(label='File Name',max_length=100)
	term = forms.CharField(label='term',max_length=100)