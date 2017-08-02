#!/usr/bin/python
# _*_ coding: utf-8 _*_

import socket
port = 8888
host = "192.168.27.128"


def client(len=0):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((host, port))
    sock.send("a"*len)
    data = sock.recv(1024)[:-1]
    print map(hex, map(ord, data))
    sock.close()


def arg_help():
    exec_cmd = "exec e.g: %s 100" % sys.argv[0]
    print exec_cmd
    sys.exit(0)


if "__main__" == __name__:
    import sys
    if len(sys.argv) != 2:
        arg_help()
    try:
        client(int(sys.argv[1]))
    except:
        arg_help()

