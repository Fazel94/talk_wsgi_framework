#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server

def application(environ, start_response):
    # Get the path from the WSGI environment
    path = environ.get('PATH_INFO', '/')
    
    # Set the default response
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)

    # Routing based on the path
    if path == '/':
        return [b"<h1>Welcome to the Home Page!</h1>"]
    elif path == '/about':
        return [b"<h1>About Us</h1><p>This is a simple WSGI microframework.</p>"]
    elif path == '/contact':
        return [b"<h1>Contact Us</h1><p>Email us at contact@example.com</p>"]
    else:
        status = '404 Not Found'
        start_response(status, headers)
        return [b"<h1>404 Not Found</h1><p>The page you are looking for does not exist.</p>"]

if __name__ == '__main__':
    # Create a WSGI server and serve the application
    server = make_server('localhost', 8000, application)
    print("Serving on http://localhost:8000...")
    server.serve_forever()

