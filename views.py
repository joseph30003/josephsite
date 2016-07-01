from django.shortcuts import *

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, loader,RequestContext
from .models import words
from .forms import NameForm
import xml.etree.ElementTree as ET
from .render import XmlDictConfig
import json

def index(request):
    t = loader.get_template('index.html')
    d = Context({'person':{'first_name':'qin'}})
    return HttpResponse(t.render(d))

def get_name(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			message = 'hello'
			return HttpResponse(json.dumps({'message':message}))
	else:
		form = NameForm()
	return render_to_response('name.html',{'form':form},RequestContext(request))

def show_file(request):
	xmldir="C:/Users/310246089/Desktop/PTEN/latest/"
	filename =xmldir + request.POST['your_name']+".xml"
	word = request.POST['term']
	tree = ET.parse(filename)
	root = tree.getroot()
	word = " "+word+" "
	xmldict = XmlDictConfig(root,word)
	t = loader.get_template('ctcontents.html')
	c = Context(xmldict)
	return HttpResponse(t.render(c))


