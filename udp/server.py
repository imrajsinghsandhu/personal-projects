import socket

'''
a udp connection is a socketless connection
we do not need to create a tunnel connection or perform 3 way handshake 
to create a reliable connection with a server unlike TCP/IP
'''
def main():

    # In summary, AF_INET is used to specify the address family (IPv4 in this case
    # SOCK_DGRAM is used to specify the socket type (datagram socket in this case, which uses the UDP protocol)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    localIP = "127.0.0.1"
    port = 8000 # must be a number
    sock.bind((localIP, port)) # binding is done when you want to receive incomping data to that address

    packetCount = 1

    # keep the port hot, open to receiving messages from clients
    while True:
        
        # refers to the maximum num of bytes to be received in a single packet
        # max of 64kB for non ethernet networks 
        bufferSize = 1024

        # recvfrom will receive data from incoming message for up to bufferSize bytes
        # excess will be truncated, so send data in packets of bufferSize bytes
        data, address = sock.recvfrom(1024)

        print("rec'd message from {}: {}".format(address, data.decode("utf-8")))
        
        # reply with the packet size in bytes
        length = len(data)

        # now reply to the client
        replyMessage = "Hello friend! Thanks for packet no. {}, size : {}!".format(packetCount, length)
        sock.sendto(replyMessage.encode("utf-8"), address)
        packetCount += 1


if __name__ == '__main__':
    main()