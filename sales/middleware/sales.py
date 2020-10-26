from .. import settings
from django.conf import settings
from django.utils.deprecation import MiddlewareMixin


class SalesMiddleware(MiddlewareMixin):

    @staticmethod
    def process_response(request, response):
        salesID = request.GET.get(settings.SALES_LINK_PARAMETER, '')
        if salesID:
            response.set_cookie(settings.SALES_COOKIE_NAME, salesID, settings.SALES_COOKIE_MAX_AGE)
        return response
