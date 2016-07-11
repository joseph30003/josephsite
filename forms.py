from django import forms
from .models import Query,Answer,Sections,Characters

def createChoice(lists):
    foo=()
    for str in lists:
        foo = foo+((str,str),)
    return foo+(('','SELECT'),)

class NameForm(forms.Form):
	file_id = forms.CharField(label='Trial ID',max_length=100)
	term = forms.CharField(label='Searching word',max_length=100)

class SearchForm(forms.ModelForm):


	class Meta:
		model = Query
		fields = ['disease', 'age', 'gender', 'gene', 'aas', 'stage', 'grade', 'address']
		labels = {
			'disease' : 'Disease Name',
		}


class questionForm(forms.ModelForm):

	class Meta:
		model = Answer
		fields = '__all__'
		labels = {
			'eligibility' : 'Is the patient eligible for this trial',
			'character' : 'What characteristics of the patient’s profile make him/her (in)eligible',
			'section' : 'What section(s) of the clinical trial document allowed you to render this decision',
			'sentence' : 'What sentence(s) of these section(s) allowed you to render this decision',
			'comment' : 'Any additional comment(s)?'
		}

	def __init__(self, *args, **kwargs):
		super(questionForm, self).__init__(*args, **kwargs)
		self.fields['section'].widget = forms.CheckboxSelectMultiple()
		self.fields['section'].queryset = Sections.objects.all()
		self.fields['character'].widget = forms.CheckboxSelectMultiple()
		self.fields['character'].queryset = Characters.objects.all()

class QueryForm(forms.ModelForm):
	class Meta:
		model = Query
		fields = ['disease','age','gender','gene','aas','stage','grade','address']

