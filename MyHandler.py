#!/usr/bin/env python

import SimpleHTTPServer
import sys
from urlparse import urlparse

def gravy():
    return 'hello dude'

# When you're not debugging you can use this handler directly.
class MyHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def __init__(self, request, client_address, server, fake=False):
        """Takes the regular constructor arguments of
SimpleHTTPServer.SimpleHTTPRequestHandler, plus one additional, optional one.  If fake
is set to true, then the class reverts to a special mode designed to be run by
the special reloading handler."""
        if fake == False:
            SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, client_address, server)
        pass
    
    def do_GET(self, up=None):
        """The argument up can be set by the reloading handler, which takes care of
setting up most of the HTTP machinery.  Otherwise, it should be left alone."""
        print "In do_GET"
        if up == None:
            rh = self
        else:
            rh = up
            pass
        rh.send_response(200)
        rh.send_header('Content-type', 'text/html')
        rh.end_headers()
        rh.wfile.write(gravy())
        print "done with do_GET"
        return
    pass

def handler():
    return MyHandler
