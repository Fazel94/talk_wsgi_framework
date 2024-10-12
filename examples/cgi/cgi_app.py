#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi

def application(environ, start_response):
    print(environ)
    status = '200 OK'
    output = b'<html><body><h1>Hello, World!</h1></body></html>'

    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(output)))
    ]
    start_response(status, response_headers)

    return [output]

if __name__ == '__main__':
    from wsgiref.handlers import CGIHandler
    CGIHandler().run(application)

