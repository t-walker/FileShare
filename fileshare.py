import os
import sys
import socket

from hashing import directory_2_hash

def client(local_directory, network_address, network_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((network_address, network_port))
    print("Connected to server")
    directory_2_hash(local_directory)

    return


def server(local_directory, network_address, network_port, user):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((network_address, network_port))
    print("Connected to client")
    directory_2_hash(local_directory)
    return


def main():
    #Main Variable Initialization
    config_file = "config.txt"
    mode = ""

    #Check to see if the user is requesting a client or server
    if sys.argv[1] == "client":
        mode = "client"
    elif sys.argv[1] == "server":
        mode = "server"
    else:
        print("Bad options.")
        return

    #Check to see if a config file exists.
    # If it does, use it.
    # Else, create it.
    if os.path.isfile(config_file):
        config_f = open("config.txt", "r")
        configuration = config_f.readlines()
        #Check to see if configuration is greater than 3 lines.
        #  If it is, it's bad.
        if len(configuration) > 3:
            print("Bad configuration.")
            return 0
        local_directory = configuration[0].split("~")[1].strip()
        network_address = configuration[1].split("~")[1].strip()
        network_port = configuration[2].split("~")[1].strip()
        user = configuration[3].split("~")[1].strip()
    else:
        print("Please set configuration")
        local_directory = input("Please enter a local directory for use: ")
        network_address = input("Please enter a remote address to use: ")
        network_port = input("Please enter a remote network port to use: ")
        user = input("Please enter user ID: ")
        print("Assembling config file. (Delete to reinitialize)")
        config_f = open("config.txt", "w")
        print("Local Directory: ", local_directory, file=config_f)
        print("Network Address: ", network_address, file=config_f)
        print("Network Port: ", network_port, file=config_f)
        print("User: ", user, file=config_f)

    if mode == "client":
        if not os.path.exists(local_directory):
            os.mkdir(local_directory)
        client(local_directory, network_address, network_port)

    if mode == "server":
        if not os.path.exists(local_directory):
            os.mkdir(local_directory)
        server()
    return 0

if __name__ == "__main__":
    main()
