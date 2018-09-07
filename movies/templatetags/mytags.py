from django import template

register = template.Library()


@register.filter(name='get_item')
def get_item(dictionary, key):
    return dictionary.get(key, '')


@register.filter(name='get_int')
def get_int(data):
    try:
        data = int(data)
    except ValueError:
        pass
    return data
