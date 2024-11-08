import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 3080))
server_socket.listen(10)
print("Server is listening...")
client_socket, client_address = server_socket.accept()
# client_socket_2, client_address_2 = server_socket.accept()
print(f"Connected with {client_address}")
# print(f"Connected with {client_address_2}")
while True:
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from client one: {data}")
    if data.lower() == 'exit':
        print('Exiting server...')
        break
    msg = input("Your message: ")
    client_socket.send(msg.encode('utf-8'))

#SECOND CLIENT 
    # data2 = client_socket_2.recv(1024).decode('utf-8')
    # print(f"Received from client two: {data2}")
    # if data2.lower() == 'exit':
    #     print('Exiting server...')
    #     break
    # msg2 = input("Your message: ")
    # client_socket_2.send(msg2.encode('utf-8'))


    if msg.lower() == 'exit':
        print('Exiting server...')
        break
client_socket.close()
# client_socket_2.close()
server_socket.close()
