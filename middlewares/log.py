# coding=utf-8

__author__ = 'mayor'

import logging

from django.utils.deprecation import MiddlewareMixin


errorlog = logging.getLogger("errorlog")
accesslog = logging.getLogger("accesslog")


class LogMiddleare(MiddlewareMixin):

    def process_request(self, request):
        accesslog.info('{req_path}'.format(req_path=request.path_info))

    def process_exception(self, request, exception):
        print(dir(request), dir(exception))
        errorlog.error('|{req_path}|{error}'.format(req_path=request.path, error=exception.args[0]))

