import os
import sys

def client(local_directory):
    os.chdir(local_directory)

    return


def server(local_directory):
    os.chdir(local_directory)
    return


def main():
    config_file = "config.txt"
    mode = ""
    if sys.argv[1:] == "client":
        mode = "client"
    if sys.argv[1:] == "server":
        mode = "server"
    else:
        print("Bad options.")

    if os.path.isfile(config_file):
        pass
    else:
        print("Please set configuration")
        local_directory = input("Please enter a local directory for use: ")
        network_address = input("Please enter a remote address to use: ")
        network_port = input("Please enter a remote network port to use: ")
        print("Assembling config file. (Delete to reinitialize)")
        config_f = open("config.txt", "w")
        print("Local Directory: ", local_directory, file=config_f)
        print("Network Address: ", network_address, file=config_f)
        print("Network Port: ", network_port, file=config_f)


    return

if __name__ == "__main__":
    main()
