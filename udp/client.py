import socket
import server
import math

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

server_bufferSize = server.bufferSize
# send a message to the server

# read txtfile
fileContents = open("transferText.txt", "r")
message = fileContents.read()
message_bytes = message.encode("utf-8")
print("length of message in bytes: {}".format(len(message_bytes))) 

# Split the string into fixed-size chunks
chunks = [message_bytes[i:i+server_bufferSize] for i in range(0, len(message_bytes), server_bufferSize)]
num_iters_for_full_transfer = len(chunks)
# iterate for num_iters_for_full_transfer of times to fully transfer the message

packetsReceived = 0

for i in range(0, num_iters_for_full_transfer):
    # will transfer each packet
    sock.sendto(chunks[i], (localIP, port))

    data, addr = sock.recvfrom(1024)

    dataSize = data.decode("utf-8")
    packetsReceived = dataSize

if ((int(packetsReceived) * server_bufferSize) < num_iters_for_full_transfer):
    print("PACKET LOSTTTT")
else :
    print("Alls good")

# # close the socket
# sock.close()