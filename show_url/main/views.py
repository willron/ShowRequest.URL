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
        url_patterns = []
        for k, v in request.GET.items():
            url_patterns.append('{}={}'.format(k, v))
        if url_patterns:
            all_patterns = '?' + '&'.join(url_patterns)
            return HttpResponse(scheme + '://' + host + cici + all_patterns)
        else:
            return HttpResponse(scheme + '://' + host + cici)

    else:
        cici = request.POST
        post_dict = {}
        for (k, v) in cici.items():
            post_dict[k] = v
        return HttpResponse('{}\nPOST\n{}\n'.format(request.scheme + '://' + request.get_host() + request.path, post_dict))
