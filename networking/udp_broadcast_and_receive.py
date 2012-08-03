#!/usr/bin/env python
#Based on https://vizible.wordpress.com/2009/01/31/python-broadcast-udp/
import socket

# Define a port to be used for the transmission
PORT = 5000

def listen():
    """Listens for incoming UDP messages, forever"""
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    my_socket.bind(('', PORT))

    while True :
        message , address = my_socket.recvfrom(8192)
        print 'message (%s) from : %s' % ( str(message), address[0])
        
def send(message):
    """Sends a single message to be broadcasted over UDP"""
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST,1)
    my_socket.sendto(message, ('<broadcast>', PORT))
    my_socket.close()