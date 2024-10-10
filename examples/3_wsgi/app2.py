#!/usr/bin/env python
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
import urllib.parse

def get_home(query_params):
    # Create a response that includes the query parameters
    response = "<h1>Welcome to the Home Page!</h1>"
    if query_params:
        response += "<h2>Query Parameters:</h2><ul>"
        for key, value in query_params.items():
            response += f"<li>{key}: {', '.join(value)}</li>"
        response += "</ul>"
    return response.encode('utf-8')  # Ensure response is bytes

def get_about():
    return b"<h1>About Us</h1><p>This is a simple WSGI microframework.</p>"

def post_contact(post_params):
    response = "<h1>Contact Form Submitted</h1><p>Data:</p><ul>"
    for key, value in post_params.items():
        response += f"<li>{key}: {', '.join(value)}</li>"
    response += "</ul>"
    return response.encode('utf-8')  # Ensure response is bytes

# Define routes
routes = {
    'GET': {
        '/': get_home,
        '/about': get_about,
    },
    'POST': {
        '/contact': post_contact,
    }
}

def application(environ, start_response):
    # Get the request method and path
    method = environ.get('REQUEST_METHOD', 'GET')
    path = environ.get('PATH_INFO', '/')

    # Set the default response
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]

    # Parse query parameters for GET requests
    query_params = {}
    if method == 'GET':
        query_string = environ.get('QUERY_STRING', '')
        query_params = urllib.parse.parse_qs(query_string)

    # Parse POST data for POST requests
    post_params = {}
    if method == 'POST':
        content_length = int(environ.get('CONTENT_LENGTH', 0))
        post_data = environ['wsgi.input'].read(content_length).decode('utf-8')
        post_params = urllib.parse.parse_qs(post_data)

    # Check if the method and path are in the routes
    if method in routes and path in routes[method]:
        if method == 'GET':
            response_body = routes[method][path](query_params)
        else:  # POST
            response_body = routes[method][path](post_params)
    else:
        status = '404 Not Found'
        response_body = b"<h1>404 Not Found</h1><p>The page you are looking for does not exist.</p>"

    start_response(status, headers)
    return [response_body]

if __name__ == '__main__':
    # Create a WSGI server and serve the application
    server = make_server('localhost', 8000, application)
    print("Serving on http://localhost:8000...")
    server.serve_forever()

