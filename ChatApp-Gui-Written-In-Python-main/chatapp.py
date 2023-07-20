import socket
import threading

# Server configuration
HOST = '127.0.0.1'
PORT = 5558
BUFFER_SIZE = 4096

# Keep track of all connected clients
clients = []

# Function to handle client connections
def handle_client(client_socket):
    while True:
        try:
            # Receive message from client
            message = client_socket.recv(BUFFER_SIZE)
            # Broadcast message to all other clients
            for client in clients:
                if client is not client_socket:
                    client.send(message)
        except:
            # Remove the client from the list of clients
            clients.remove(client_socket)
            # Close the client socket
            client_socket.close()
            break

# Create a server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server listening on {HOST}:{PORT}")

while True:
    # Accept a new client connection
    client_socket, addr = server_socket.accept()
    print(f"Accepted connection from {addr[0]}:{addr[1]}")
    # Add the client to the list of clients
    clients.append(client_socket)
    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()
