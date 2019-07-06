import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "192.168.1.2"
port = 445

def portscanner(port):
    if sock.connect_ex((host,port)):
            print "port %d is closed" % (port)
    else:
            print "port %d is open" % (port)
portscanner(port)