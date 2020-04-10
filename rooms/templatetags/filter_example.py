from django import template

register = template.Library()


@register.filter
def example(value_from_template):
    new_value = value_from_template.capitalize()
    return new_value
