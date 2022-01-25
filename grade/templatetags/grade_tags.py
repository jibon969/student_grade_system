from django import template

register = template.Library()


@register.filter(name='grade_counter_id')
def grade_counter(value, page):
    value, page = int(value), int(page)
    adjusted_value = value + (page - 1) * 5
    return adjusted_value