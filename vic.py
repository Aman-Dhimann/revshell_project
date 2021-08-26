import socket
import subprocess

#listening for ipv4 and tcp
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))

#max 2 connections
s.listen(2)

client, addr = s.accept()
cmd = client.recv(2048).decode()

while cmd != 'quit':
    print(cmd)
    cmd = str(cmd)

    result = subprocess.check_output(cmd, shell=True)
    print(result)
    client.send(result)
    cmd = client.recv(2048).decode()
cmd.close()
s.close()



