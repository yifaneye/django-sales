from . import settings
from django.conf import settings
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def get_sales(salesID):
    try:
        salesUser = User.objects.get(id=salesID)
        return salesUser
    except (ValueError, ObjectDoesNotExist):
        return get_sales(settings.SALES_DEFAULT_ID)


def sales(request):
    salesID = request.GET.get(settings.SALES_LINK_PARAMETER, '') or request.COOKIES.get(settings.SALES_COOKIE_NAME, '')
    salesUser = get_sales(salesID)
    return {"sales": salesUser}
