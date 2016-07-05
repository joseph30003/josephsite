from django import forms

class NameForm(forms.Form):
	file_id = forms.CharField(label='Trial ID',max_length=100)
	term = forms.CharField(label='Searching word',max_length=100)