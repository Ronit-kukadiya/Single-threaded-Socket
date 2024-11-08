import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 3080))
print('Connected to server')
while True:
    msg = input("Your message: ")
    client_socket.send(msg.encode('utf-8'))
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from server: {data}")
    if msg.lower() == 'exit':
        print("Exiting...")
        break
client_socket.close()