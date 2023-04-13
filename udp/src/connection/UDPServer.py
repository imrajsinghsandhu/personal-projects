from connection.UDPConnection import UDPConnection
import socket

class UDPServer(UDPConnection):
    
    def __init__(self, local_ip : str, port : int, buffer_size : int) -> None:
        super().__init__(local_ip, port, buffer_size)

    def instantiate_server(self) -> None:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((self._local_ip, self._port)) # binding is done when you want to receive incoming data to that address
        print("server socket binded...")
        print("server started...")
        packet_count = 1
        # keep the port hot, open to receiving messages from clients
        while True:
            
            # recvfrom will receive data from incoming message for up to bufferSize bytes
            # excess will be truncated, so send data in packets of bufferSize bytes
            data, address = sock.recvfrom(self._buffer_size)
            # now reply to the client with the count of packets
            replyMessage = "{}".format(packet_count)
            sock.sendto(replyMessage.encode("utf-8"), address)
            packet_count += 1
