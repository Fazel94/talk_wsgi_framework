#!/usr/bin/env python
# -*- coding: utf-8 -*-

import http.server
import os

PORT = 8005

Handler = http.server.CGIHTTPRequestHandler
Handler.cgi_directories = ["/"]

with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    httpd.serve_forever()

