from django import template

register = template.Library()

@register.filter
def add_class(value, class_name):
    """Adds a CSS class to a widget's HTML output."""
    return value.as_widget(attrs={"class": class_name})
