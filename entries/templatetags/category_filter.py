from django import template

register = template.Library()

@register.filter
def in_category(objects, category):
	return objects.filter(category=category)