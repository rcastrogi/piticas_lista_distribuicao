from django import template

register = template.Library()


@register.filter
def mul(value, arg):
    """Multiplica value por arg"""
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return 0
