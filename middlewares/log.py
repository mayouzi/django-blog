# coding=utf-8

__author__ = 'mayor'

import logging

from django.utils.deprecation import MiddlewareMixin


errorlog = logging.getLogger("errorlog")
accesslog = logging.getLogger("accesslog")


class LogMiddleare(MiddlewareMixin):

    def process_request(self, request):
        accesslog.info('{host}|{req_path}'.format(host=request.get_host(),
                                                  req_path=request.get_full_path()))

    def process_exception(self, request, exception):
        errorlog.error('|{req_path}|{error}'.format(req_path=request.get_full_path(),
                                                    error=exception.args[0]))

