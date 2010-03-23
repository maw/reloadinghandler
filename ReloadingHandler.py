#!/usr/bin/python

import SimpleHTTPServer
import sys

real_module = None

class reloading_handler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    __module = None
    __barf_on_reload_error = True
    
    def __reload(self):
        # It probably isn't necessary to wrap this in try ... except,
        # because we've already tried once.  Also, SimpleHTTPServer is robust
        # against exceptions inside its handlers.
        #
        # XXX: Is there a need for the following?
        # for key in sys.modules.keys():
        #     reload(sys.modules[key])
        reload(self.__module)
        pass
    
    # Other methods, as necessary, will look much like this one.
    def do_GET(self):
        self.__reload()
        self.__module.do_GET(self)
        pass
    
    def __init__(self, request, client_address, server):
        try:
            self.__module = real_module
            reload(self.__module)
        except TypeError, te:
            print "Failed to load module ", `self.__module`, ": ", `te`
            # XXX: Anything possible other than just bailing here?
            # XXX: For that matter, should we bail at all?
            sys.exit(1)
            pass
        
        SimpleHTTPServer.SimpleHTTPRequestHandler.__init__(self, request, client_address, server)
        pass
    
    
def handler():
    return reloading_handler
