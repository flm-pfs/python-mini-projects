import socket
import threading

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

nickname = input("Choose a nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

running = True  # Global flag to control thread execution

def receive():
    global running
    while running:
        try:
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                print(message)
                if 'Server is shutting down...' in message:
                    running = False
        except:
            print("An error occurred!")
            running = False


def write():
    global running
    while running:
        message = input('')
        if message.strip().lower() == 'bye':
            client.send(message.encode('ascii'))
            running = False
        else:
            client.send(f'{nickname}: {message}'.encode('ascii'))

receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()

receive_thread.join()
write_thread.join()
client.close()  # Ensure the socket is closed after threads have finished
