#!/usr/bin/env python
# -*- coding: utf-8 -*-

from mod_python import apache

def index(req):
    req.content_type = "text/html"
    return """
        <html>
            <head>
                <title>Mod Python Example</title>
            </head>
            <body>
                <h1>Welcome to the Mod Python Example!</h1>
                <p>This is a simple web application built using the Mod Python module.</p>
            </body>
        </html>
    """

def hello(req, name="World"):
    req.content_type = "text/html"
    return f"<h1>Hello, {name}!</h1>"

