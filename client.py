import socket
HOST='192.168.29.113'
PORT=9090
c_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c_socket.connect((HOST,PORT))
c_socket.send(" hey i am kratika".encode('utf-8'))
print(c_socket.recv(1024).decode('utf-8'))