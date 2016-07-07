from django import forms

def createChoice(lists):
    foo=()
    for str in lists:
        foo = foo+((str,str),)
    return foo+(('','SELECT'),)

class NameForm(forms.Form):
	file_id = forms.CharField(label='Trial ID',max_length=100)
	term = forms.CharField(label='Searching word',max_length=100)

class SearchForm(forms.Form):
	Gender_list = ['Male','Female','Both']
	Stage_list = ['Stage I','Stage II','Stage III','Stage IV','Stage X','Stage IA','Stage IIA','Stage IIIA','Stage IVA','Stage IB','Stage IIB','Stage IIIB','Stage IVB','Stage IC','Stage IIC','Stage IIIC','Stage IVC']
	Grade_list = ['Grade 1','Grade 2','Grade 3','Grade 4','Grade I','Grade II','Grade III','Grade IV']
	disease = forms.CharField(label='Enter the disease of the patient',max_length=100,required=False,widget=forms.TextInput(attrs={'placeholder':'Disease Name'}))
	age = forms.CharField (label='Age in years',required=False,max_length=2,widget=forms.TextInput(attrs={'placeholder':'Age'}))
	gender = forms.ChoiceField(choices=createChoice(Gender_list),label="Gender")
	gene = forms.CharField(label="Gene Mutation",required=False,max_length=100,widget=forms.TextInput(attrs={'placeholder':'Gene Name'}))
	aas = forms.CharField(label="Amino Acid Substitution", required=False,max_length=100,widget=forms.TextInput(attrs={'placeholder':'Amino Acid Substitution'}))
	stage = forms.ChoiceField(choices=createChoice(Stage_list), label="Stage")
	grade = forms.ChoiceField(choices=createChoice(Grade_list), label="Grade")
	address = forms.CharField(label='Address', max_length=100, required=False,widget=forms.TextInput(attrs={'placeholder': 'Address'}))

class questionForm(forms.Form):
	sentence = forms.CharField(label='which sentence you think is correct',max_length=300,required=False)
	answer= forms.ChoiceField(choices=(('true','true'),('false','false')), label="choose your answer")
	words = forms.CharField(label='which word is not correct', max_length=300, required=False)