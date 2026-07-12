import socket
HOST='192.168.29.113'
PORT=9090
c_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

try:
   c_socket.connect((HOST,PORT))
   print(f"Connected to the server at{HOST}:{PORT}")

   while True:
    message=input("client: ")
    c_socket.send(message.encode('utf-8'))
    if message.lower() == "exit":
     print("you ended the chat")
     break
    data = c_socket.recv(1024)
    if not data:
       print("Server disconnected.")
       break
    
    reply = data.decode("utf-8")
    print(f"Server : {reply}")

except Exception as e:
 print(f"Error: {e}")

finally:
 c_socket.close()
 print("Connection closed.")

print(f"Connected to the server at{HOST}:{PORT}")