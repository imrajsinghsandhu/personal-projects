import sys
from src.connection.UDPClient import UDPClient

'''
Main file that handles the CLI-arguments and calls the sub class in this project
'''

# is args present?
def is_args_present() -> bool:
    print ("length of args : {}".format(len(sys.argv)))
    if (len(sys.argv) > 1):
        return True
    else: 
        return False

# main will accept command line arguments
def main():
    data_visualisation_requested : bool = False

    if (is_args_present()):
        data_visualisation_requested = True
    
    print("Data Visualisation? : {}".format(data_visualisation_requested))
    
    # instantiate the UDPConnection class
    local_ip : str = "127.0.0.1"
    port : int = 8000
    buffer_size : int = 60000

    udp_client : UDPClient = UDPClient(request_data_vis=data_visualisation_requested, local_ip=local_ip, port=port, buffer_size=buffer_size)
    udp_client.create_client_connection()
    print("client sent")


if __name__ == '__main__':
    main()