from django import template

register = template.Library()


@register.filter(name='arrow')
def arrow(value):
    if value == 'asc':
        return '↑'
    else:
        return '↓'
