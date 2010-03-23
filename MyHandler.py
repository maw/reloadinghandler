#!/usr/bin/env python

import SimpleHTTPServer
import sys
from urlparse import urlparse

def gravy():
    return 'hello dude'

# The real meat of a handler.  It gets its own function for now, but I'd like to
# fix this eventually.
def do_GET(real_handler):
    print "In the real do_GET"
    real_handler.send_response(200)
    real_handler.send_header('Content-type', 'text/html')
    real_handler.end_headers()
    real_handler.wfile.write(gravy())
    return

# When you're not debugging you can use this handler directly.
class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, client_address, server)
        pass
    def do_GET(self):
        do_GET(self)
    pass
