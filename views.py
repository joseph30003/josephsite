from django.shortcuts import *

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader, RequestContext
from .models import words
from .forms import NameForm, SearchForm, questionForm, QueryForm
import xml.etree.ElementTree as ET
import xmltodict
import json, requests


def index(request):
	t = loader.get_template('index.html')
	d = Context({'person': {'first_name': 'qin'}})
	return HttpResponse(t.render(d))


def get_menu(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			message = 'hello'
			return HttpResponse(json.dumps({'message': message}))
	else:
		form = NameForm()
	return render_to_response('trail_highlight.html', {'form': form}, RequestContext(request))


def show_file(request):
	import urllib.request as ur
	xml_url = 'https://clinicaltrials.gov/show/' + request.POST['file_id'] + '?resultsxml=true'
	data = ur.urlopen(xml_url).read()
	xmldict = xmltodict.parse(data)

	t = loader.get_template('ctcontents.html')

	return HttpResponse(t.render(xmldict))


def vl_result(request):
	ls = []
	disease = ''
	gene = ''
	age = ''
	gender = ''
	aas = ''
	stage = ''
	grade = ''

	if request.method == 'POST':
		form = questionForm()
		title = 'questions'
		disease = request.POST['disease']
		gene = request.POST['gene']
		age = request.POST['age']
		gender = request.POST['gender']
		aas = request.POST['aas']
		stage = request.POST['stage']
		grade = request.POST['grade']
		address = request.POST['address']

		# added here but should be put in a config file
		use_should = False
		multi_match_type = 'cross_fields'
		multi_match_operator = 'and'
		boost_must_value = 3
		boost_should_value = 0.1

		body = {}
		body["query"] = {}
		body["query"]["bool"] = {}
		body["query"]["bool"]["must"] = []
		body["query"]["bool"]["should"] = []

		body["highlight"] = {}
		body["highlight"]["fields"] = {}
		body["highlight"]["fields"]["Purpose"] = {"number_of_fragments": 0}
		body["highlight"]["fields"]["official_title"] = {"number_of_fragments": 0}
		body["highlight"]["fields"]["brief_title"] = {"number_of_fragments": 0}
		body["highlight"]["fields"]["description"] = {"number_of_fragments": 0}
		body["highlight"]["fields"]["Inclusion Criteria"] = {"number_of_fragments": 0}
		body["highlight"]["fields"]["Conditions"] = {"number_of_fragments": 0}
		body["highlight"]["fields"]["Exclusion Criteria"] = {"number_of_fragments": 0}
		body["highlight"]["pre_tags"] = ["<mark>"]
		body["highlight"]["post_tags"] = ["</mark>"]
		if disease:
			body["query"]["bool"]["must"].append({
				"multi_match":
					{
						"query": disease,
						"type": multi_match_type,
						"boost": boost_must_value,
						"operator": multi_match_operator,
						"fields": ["Purpose", "description", "Inclusion Criteria", "official_title", "brief_title",
						           "Conditions",
						           "Purpose.whitespace", "description.whitespace", "Inclusion Criteria.whitespace",
						           "official_title.whitespace", "brief_title.whitespace", "Conditions.whitespace"]}})
			if use_should:
				body["query"]["bool"]["should"].append({
					"multi_match": {
						"query": disease,
						"boost": boost_should_value,
						"fields": ["Exclusion Criteria", "Exclusion Criteria.whitespace", "Exclusion Criteria.normal"]
					}

				})
		if gene:
			body["query"]["bool"]["must"].append({
				"multi_match":
					{
						"query": gene,
						"boost": boost_must_value,
						"fields": ["Purpose", "description", "Inclusion Criteria", "official_title", "brief_title",
						           "Conditions",
						           "Purpose.whitespace", "description.whitespace", "Inclusion Criteria.whitespace",
						           "official_title.whitespace", "brief_title.whitespace", "Conditions.whitespace"]}})
			if use_should:
				body["query"]["bool"]["should"].append({
					"multi_match": {
						"query": gene,
						"boost": boost_should_value,
						"fields": ["Exclusion Criteria", "Exclusion Criteria.whitespace", "Exclusion Criteria.normal"]
					}
				})
		if age:
			body["query"]["bool"]["must"].append({
				"range": {
					"maximumAge": {"gte": int(age) * 365 * 24 * 60}}})
			body["query"]["bool"]["must"].append({
				"range": {
					"minimumAge": {"lte": int(age) * 365 * 24 * 60}}})
		body["query"]["bool"]["must"].append({"bool": {}})
		body["query"]["bool"]["must"][-1]["bool"]["should"] = []

		if gender and gender != "Select":
			body["query"]["bool"]["must"][-1]["bool"]["should"].append({
				"match": {
					"gender": gender
				}})
			body["query"]["bool"]["must"][-1]["bool"]["should"].append({
				"match": {
					"gender": "Both"
				}})
		if aas:
			body["query"]["bool"]["must"].append({
				"multi_match": {
					"query": aas,
					"boost": boost_must_value,
					"fields": ["Purpose", "description", "Inclusion Criteria", "official_title", "brief_title",
					           "Conditions",
					           "Purpose.whitespace", "description.whitespace", "Inclusion Criteria.whitespace",
					           "official_title.whitespace", "brief_title.whitespace", "Conditions.whitespace"]}})
			if use_should:
				body["query"]["bool"]["should"].append({
					"multi_match": {
						"query": aas,
						"boost": boost_should_value,
						"fields": ["Exclusion Criteria", "Exclusion Criteria.whitespace", "Exclusion Criteria.normal"]
					}
				})
		if stage != '':
			body["query"]["bool"]["must"].append({
				"match": {
					"stages": stage.split(' ')[1]}})

		if grade != '':
			body["query"]["bool"]["must"].append({
				"match": {
					"grades": grade.split(' ')[1]}})

		records = requests.post('http://127.0.0.1:9200/test7/mappedTrials/_search?size=10', data=json.dumps(body))
		total = records.json()["hits"]["total"]
		records = records.json()["hits"]["hits"]

		for i in records:
			rec = {}
			for field in i:
				if field == "_source":
					rec["source"] = i[field]
				elif field == "_id":
					rec["id"] = i[field]
				else:
					rec[field] = i[field]

			ls.append(rec)

	else:
		form = SearchForm()
		title = 'search'
	return render(request, 'v_result.html',
	              {'form': form, 'records': ls, 'disease': disease, 'gene': gene, 'aas': aas, 'age': age,
	               'gender': gender, 'stage': stage, 'grade': grade, 'subtitle': title})
