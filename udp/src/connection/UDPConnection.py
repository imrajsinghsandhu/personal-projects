'''
Class will have UDP client and server children
'''
class UDPConnection:

    # Constructor for UDPConnection
    def __init__(self, _local_ip : str, _port : int, _buffer_size : int) -> None:
        # all protected methods only available for its children classes
        self._local_ip = _local_ip
        self._port = _port
        self._buffer_size = _buffer_size

    # read data from txt file
    def _read_data(self, filename : str) -> bytes:

        fileContents = open(filename, "r") # opening file in read mode
        message : str = fileContents.read()
        message_bytes : bytes = message.encode("utf-8")
        print("length of message in bytes: {}".format(len(message_bytes))) 

        return message_bytes