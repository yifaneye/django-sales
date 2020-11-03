from .. import settings
from django.conf import settings
from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def sales(context, value):
    salesUser = context.request.GET.get(settings.SALES_LINK_PARAMETER, '') or context.request.COOKIES.get(settings.SALES_COOKIE_NAME, '')
    if salesUser:
        connection = '&' if '?' in value else '?'
        value += connection + settings.SALES_LINK_PARAMETER + '=' + salesUser
    return value
