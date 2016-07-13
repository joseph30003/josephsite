from django.db import models

# Create your models here.
from django.db import models

def createChoice(lists):
    foo=()
    for str in lists:
        foo = foo+((str,str),)
    return foo+(('','SELECT'),)

class words(models.Model):
	word = models.CharField(max_length=150)
	counts = models.IntegerField()

class references(models.Model):
	word = models.CharField(max_length=150)
	file_num = models.CharField(max_length=100)

class Sections(models.Model):
	section = models.CharField(max_length=20)
	def __str__(self):
		return self.section

class Characters(models.Model):
	character = models.CharField(max_length=20)

	def __str__(self):
		return self.character

class Query(models.Model):
	Gender_list = ['Male', 'Female', 'Both']
	Stage_list = ['Stage I', 'Stage II', 'Stage III', 'Stage IV', 'Stage X', 'Stage IA', 'Stage IIA', 'Stage IIIA',
	              'Stage IVA', 'Stage IB', 'Stage IIB', 'Stage IIIB', 'Stage IVB', 'Stage IC', 'Stage IIC',
	              'Stage IIIC', 'Stage IVC']
	Grade_list = ['Grade 1', 'Grade 2', 'Grade 3', 'Grade 4', 'Grade I', 'Grade II', 'Grade III', 'Grade IV']
	disease = models.CharField(max_length=100,blank=True,null=True)
	age = models.CharField(max_length=3,blank=True,null=True)
	gender = models.CharField(max_length=6,choices=createChoice(Gender_list),blank=True,null=True)
	gene = models.CharField(max_length=100,blank=True,null=True)
	aas = models.CharField( max_length=100,blank=True,null=True)
	stage = models.CharField(max_length=10, choices=createChoice(Stage_list),blank=True,null=True)
	grade = models.CharField(max_length=10, choices=createChoice(Grade_list),blank=True,null=True)
	address = models.CharField(max_length=100,blank=True,null=True)
	resultNUM = models.IntegerField(blank=True,null=True)

	def __str__(self):
		return self.disease

class Answer(models.Model):
	Eligibility_list = ((True,'YES'),(False,'NO'))
	Character_list = ['disease','age','gender','stage','grade','gene','mutation']
	query = models.ForeignKey(Query,default=0)
	queryID = models.CharField(max_length=20,blank=True,null=True)
	clinicalTrial = models.CharField(max_length=20)
	eligibility = models.BooleanField(choices=Eligibility_list)
	character = models.ManyToManyField(Characters)
	section = models.ManyToManyField(Sections)
	sentence = models.TextField(blank=True,null=True)
	comment = models.TextField(blank=True,null=True)
	author = models.CharField(max_length=20,blank=True, null=True)
	time = models.IntegerField(blank=True,null=True)

class GeneSyn(models.Model):
	gene = models.CharField(max_length=150)
	synonyms = models.CharField(max_length=150,blank=True,null=True)