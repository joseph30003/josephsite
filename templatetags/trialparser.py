from django import template

register = template.Library()
@register.filter(name = 'txt')
def txt(value):
	return value['#text']