from connection.UDPConnection import UDPConnection
import time
import socket

class UDPClient(UDPConnection):

    def __init__(self, request_data_vis : bool, local_ip : str, port : int, buffer_size : int) -> None:
        self.request_data_vis = request_data_vis # for own attribute
        super().__init__(local_ip, port, buffer_size) # for parent constructor
    
    def _send_message_to_server(self, chunks, sock, num_iters) -> None:
        '''
        This is an internal method and should not be called outside of scope of this class
        '''
        packetsReceived = 0
        timestamp_start = time.time()
        for i in range(0, num_iters):
            # will transfer each packet
            sock.sendto(chunks[i], (self._local_ip, self._port))

            data, addr = sock.recvfrom(1024)

            dataSize = data.decode("utf-8")
            packetsReceived = dataSize

        timestamp_end = time.time()

        diff_time = timestamp_end - timestamp_start # in seconds

        if ((int(packetsReceived) * self._buffer_size) < num_iters):
            print("PACKET LOSTTTT")
        else :
            print("Alls good")

        # printing time taken for callback
        print("Time taken : {:.5f} seconds".format(diff_time))

    # instantiate the client
    def create_client_connection(self) -> None:

        sock : socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # read txtfile, return the contents in bytes form
        message_in_bytes : bytes = self._read_data("data/transferText.txt")

        # Split the string into fixed-size packets
        chunks = [message_in_bytes[i:i+self._buffer_size] for i in range(0, len(message_in_bytes), self._buffer_size)]
        num_iters_for_full_transfer = len(chunks)

        self._send_message_to_server(chunks, sock, num_iters_for_full_transfer)
