from django.db import models

# Create your models here.
from django.db import models

class words(models.Model):
	word = models.CharField(max_length=150)
	counts = models.IntegerField()

class references(models.Model):
	word = models.CharField(max_length=150)
	file_num = models.CharField(max_length=100)