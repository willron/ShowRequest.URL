#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
by:willron
'''
__author__ = '郑绪鹏'


from django.http import HttpResponse


def index(request):
    if request.method == 'GET':
        cici = request.path
        host = request.get_host()
        scheme = request.scheme
        return HttpResponse(scheme + '://' + host + cici)

    else:
        pass
