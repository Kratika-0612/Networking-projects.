
import socket
import threading

HOST='192.168.29.113'
PORT=9090
server_socket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_socket.bind((HOST,PORT))

server_socket.listen()
print(f"Server is listening on {HOST}:{PORT}")

def handle_client(client_socket):
    try:
        while True:
            data=client_socket.recv(1024)
            if not data:
                print("client disconnected")
                break
            message=data.decode('utf-8')

            print(f"\n client : {message}")

            if message.lower() == "exit":
                print("Client ended the chat.")
                break

            reply = input("Server : ")

            client_socket.send(reply.encode("utf-8"))

            if reply.lower() == "exit":
                print("Server ended the chat.")
                break


    except Exception as e:

        print(f"Error : {e}")

    finally:

        client_socket.close()

        print("Connection closed.\n")
            

while True:
    client_socket,address=server_socket.accept()

    print(f"connected to",{address})
    
    thread = threading.Thread(
        target=handle_client,
        args=(client_socket,)
    )

    thread.start()

