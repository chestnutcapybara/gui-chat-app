import socket
import threading

# Host and port stuff
HOST = '0.0.0.0'
PORT = 5000

# Create the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

# List of connected clients
clients = []

# Function to handle client connections
def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

def handle_client(client):
    while True:
        try:
            message = client.recv(1024)
            if message:
                broadcast(message, client)
            else:
                raise Exception("Client disconnected")
        except Exception as e:
            print("A client has disconnected: ", e)
            clients.remove(client)
            client.close()
            break

