#!/usr/bin/python
# _*_ coding: utf-8 _*_

import socket
port = 8888
host = "192.168.27.128"


def client(len=None, date=None):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((host, port))
    if len is not None:
        sock.send("a"*len)
    else:
        sock.send(date)
    data = sock.recv(1024)[:-1]
    print map(hex, map(ord, data))
    sock.close()


def arg_help():
    print "exec e.g: %s -L 100" % sys.argv[0]
    print "exec e.g: %s -D abcdefg" % sys.argv[0]
    sys.exit(0)


if "__main__" == __name__:
    import sys
    if len(sys.argv) != 3:
        arg_help()
    try:
        if "-L" in sys.argv:
            client(len=int(sys.argv[2]))
        elif "-D" in sys.argv:
            client(date=sys.argv[2])
    except:
        arg_help()
