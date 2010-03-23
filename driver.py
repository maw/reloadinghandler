#!/usr/bin/python
# -*- coding: utf-8 -*-

import SimpleHTTPServer
import SocketServer
import socket
import sys

import MyHandler
import ReloadingHandler

def main(args):
    PORT = 8000
    
    # Tell the reloading handler which module contains the  real handler into
    # which it should call.  The module in question needs to provide a 
    # a function handler() which returns your handling class.
    ReloadingHandler.real_module = MyHandler
    
    SocketServer.ThreadingTCPServer.allow_reuse_address = True
    
    ## When you're developing and testing
    httpd = SocketServer.ThreadingTCPServer(('localhost', PORT),
                                            ReloadingHandler.handler())
    ## For production
    #httpd = SocketServer.ThreadingTCPServer(('localhost', PORT),
    #                                        MyHandler.MyHandler)
    
    httpd.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    httpd.serve_forever()
    
    pass

if __name__ == '__main__':
    sys.exit(main(sys.argv))
    pass
