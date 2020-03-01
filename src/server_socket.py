

# The parameters socket.AF_INET and socket.SOCK_STREAM determine the type of socket and protocol to be used.
# ("0.0.0.0", 8081) is the address the server should use.
# Note there is an extra set of brackets around the address, make sure you have both the inner and outer brackets on the bind function
# "0.0.0.0" will bind the socket to all network IP addresses available on this computer.
# It’s very common for a computer to have multiple network addresses:
# Typically, an internal address of 127.0.0.1, which only programs on this computer can use
# One or more external addresses such as 192.168.1.2, which can be used to connect over a network
# Although I chose to use "0.0.0.0" to bind the socket to all IP addresses, as this is useful for testing, you could use a specific IP address, for example 127.0.0.1, if you wanted this only to be available to other programs on your computer. You could also use the IP you found earlier, to allow access from outside your network.
# 8081 determines the TCP port your socket should use.
# Ports are typically used to identify the purpose of the connection and can be any number between 0 and 65535. Ports 0 to 1023 are well known ports that are usually restricted for specific uses: for example, port 80 is HTTP and shouldn’t really be used.
# I chose 8081 as it’s typically used for testing, but you could pick any number you wanted.
# When a new client connects, two parameters are returned: - A new socket, which I have called connection_socket and is the connection to the client - The network address of the client that connected, including its IP address and port
import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("0.0.0.0", 8081))
server_socket.listen()

print("waiting for connection")
connection_socket, address = server_socket.accept()
print(f"Connection with {connection_socket} and address {address}")

message = f"You are connected at {connection_socket} with address {address}"
connection_socket.send(message.encode())
print(f"{connection_socket.recv(1024).decode()}")
connection_socket.close()
server_socket.close()
