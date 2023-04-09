import socket

'''
in a nutshell, you just gotta send data to the UDP server, and that it. No verification is required.
UDP is a socket connection, its just not reliable, meaning its focused on speed, and does not have 
packet tracking or resending lost/corrupted packets

Having packet tracking and resending lost/corrupted packets adds to overhead, and is more suitable for a
service that requires a reliable connecton - such as TCP/IP

UDP is used for low latency services, and is used for systems where packet loss is allowed.
'''

# initialise the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# prep the details of the server
localIP = "127.0.0.1"
port = 8000

# send a message to the server
message = "Hey server!"
sock.sendto(message.encode("utf-8"), (localIP, port))

# process the message received from the server
bufferSize = 1024
data, address = sock.recvfrom(bufferSize)

print("received message : {} from serverAddress: {}".format(data.decode("utf-8"), address))

# close the socket
sock.close()