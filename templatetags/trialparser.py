from django import template

register = template.Library()
@register.filter(name = 'txt')
def txt(value):
	return value['#text']

@register.filter(name = 'InclusionCriteria')
def InclusionCriteria(value):
	return value['Inclusion Criteria']

@register.filter(name = 'ExclusionCriteria')
def ExclusionCriteria(value):
	return value['Exclusion Criteria']

@register.filter(name = 'years')
def years(value):
	return int(value/525600)