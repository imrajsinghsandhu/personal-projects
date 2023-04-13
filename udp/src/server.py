from src.connection.UDPServer import UDPServer

'''
Main file that handles the CLI-arguments and calls the sub class in this project
'''
# main will accept command line arguments
def main():

    # instantiate the UDPConnection class
    local_ip : str = "127.0.0.1"
    port : int = 8000
    buffer_size : int = 60000

    udp_server : UDPServer = UDPServer(local_ip=local_ip, port=port, buffer_size=buffer_size)
    udp_server.instantiate_server()


if __name__ == '__main__':
    main()