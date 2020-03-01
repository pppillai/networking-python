# Import the socket library and create a socket named client_socket.py.
# import socket
# client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# When you created the server socket, you specified that the type and protocol should be TCP/IP by using socket.AF_INET and socket.SOCK_STREAM.
# For sockets to connect they need to be of the same type, so your client needs to be set up in the same way.
# Connect to the server socket.
# client_socket.connect(("127.0.0.1", 8081))
# The address to connect to is specified as ("127.0.0.1", 8081).
# The first part, "127.0.0.1", is the IP address of the server you want to connect to. 127.0.0.1 is a special IP address and is reserved for the internal address of the computer, known as localhost.
# I have used this address as I intend to run the client and server programs on the same computer to test them. To connect to a server over a network you would change this to be the external IP address of the server.
# As you set your server up to listen to all IP addresses using 0.0.0.0, it will accept connections to both internal and external addresses.
# The second part, 8081, is the port the server socket is using.



import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect(("127.0.0.1", 8081))

print("Connected")
message = client_socket.recv(1024)
print(f"{message.decode()}")

client_socket.send("Hello Server thanks for connecting".encode())
client_socket.close()
