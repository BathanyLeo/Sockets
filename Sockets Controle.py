import socket

UDP_IP = "10.160.108.101"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

sock.connect((UDP_IP,UDP_PORT))

sock.send("cinema".encode())

msg=sock.recv(1024)
print(msg.decode())
	
