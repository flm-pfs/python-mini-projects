import socket
import threading

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432        # Port to listen on (non-privileged ports are > 1023)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []
shutdown_flag = False


def broadcast(message):
    for client in clients:
        client.send(message)


def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
            print(message.decode('ascii'))  # Print message to server console
            if message.decode('ascii').strip().lower() == 'bye':
                client.send('You have left the chat.'.encode('ascii'))
                client.close()
                remove(client)
                break
        except:
            remove(client)
            break


def remove(client):
    if client in clients:
        index = clients.index(client)
        clients.remove(client)
        client.close()
        nickname = nicknames[index]
        broadcast(f'{nickname} left the chat!'.encode('ascii'))
        nicknames.remove(nickname)


def receive():
    while not shutdown_flag:
        try:
            client, address = server.accept()
            print(f"Connected with {str(address)}")

            client.send('NICK'.encode('ascii'))
            nickname = client.recv(1024).decode('ascii')
            nicknames.append(nickname)
            clients.append(client)

            print(f"Nickname of the client is {nickname}!")
            broadcast(f"{nickname} joined the chat!".encode('ascii'))
            client.send('Connected to the server!'.encode('ascii'))

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        except:
            break


def write():
    global shutdown_flag
    while True:
        message = input('')
        if message.strip().lower() == 'shutdown':
            print("Shutting down the server...")
            shutdown_flag = True
            broadcast('Server is shutting down...'.encode('ascii'))
            for client in clients:
                client.close()
            server.close()
            break
        broadcast(f'Server: {message}'.encode('ascii'))


print("Server is listening...")

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
