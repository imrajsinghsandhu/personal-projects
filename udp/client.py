import socket
import server
import math
import time

'''
in this branch, we need to create a timestamp feature, that allows us to monitor the timestamps of callbacks from
server. 
1. Import time library
2. start a timestamp right before sending the packet, 
3. end the timestamp when call back received
4. print out the timestamp
'''

# initialise the socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# prep the details of the server
localIP = "127.0.0.1"
port = 8000

# send a message to the server
# read txtfile
fileContents = open("transferText.txt", "r")
message = fileContents.read()
message_bytes = message.encode("utf-8")
print("length of message in bytes: {}".format(len(message_bytes))) 

# Split the string into fixed-size chunks
chunks = [message_bytes[i:i+server.buffer_size] for i in range(0, len(message_bytes), server.buffer_size)]
num_iters_for_full_transfer = len(chunks)
# iterate for num_iters_for_full_transfer of times to fully transfer the message

packetsReceived = 0

timestamp_start = time.time()
for i in range(0, num_iters_for_full_transfer):
    # will transfer each packet
    sock.sendto(chunks[i], (localIP, port))

    data, addr = sock.recvfrom(1024)

    dataSize = data.decode("utf-8")
    packetsReceived = dataSize

timestamp_end = time.time()

diff_time = timestamp_end - timestamp_start # in seconds

if ((int(packetsReceived) * server.buffer_size) < num_iters_for_full_transfer):
    print("PACKET LOSTTTT")
else :
    print("Alls good")

# printing time taken for callback
print("Time taken : {:.5f} seconds".format(diff_time))

# # close the socket
# sock.close()