from django.shortcuts import *

# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from django.template import Context, loader,RequestContext
from .models import words
from .forms import NameForm
import xml.etree.ElementTree as ET
import xmltodict
import json

def index(request):
    t = loader.get_template('index.html')
    d = Context({'person':{'first_name':'qin'}})
    return HttpResponse(t.render(d))

def get_menu(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			message = 'hello'
			return HttpResponse(json.dumps({'message':message}))
	else:
		form = NameForm()
	return render_to_response('trail_highlight.html',{'form':form},RequestContext(request))

def show_file(request):
	import urllib.request as ur
	xml_url= 'https://clinicaltrials.gov/show/'+request.POST['file_id']+'?resultsxml=true'
	data = ur.urlopen(xml_url).read()
	xmldict = xmltodict.parse(data)

	t = loader.get_template('ctcontents.html')


	return HttpResponse(t.render(xmldict))

def vl_search(request):
	t = loader.get_template('index.html')
	d = Context({'person':{'first_name':'qin'}})
	return HttpResponse(t.render(d))

def vl_result(request):
	t = loader.get_template('v_result.html')
	d = Context({'person':{'first_name':'qin'}})
	return HttpResponse(t.render(d))