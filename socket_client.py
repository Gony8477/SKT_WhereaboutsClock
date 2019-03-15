import socket

HOST = "52.78.114.210"
PORT = 8089
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))

def sendingMsg():
	while True:
		data = input()
		data = bytes(data, "utf-8")
		s.send(data)
		data = s.recv(1024)
		print(data)
	s.close()


def gettingMsg():
	while True:
		data = s.recv(1024)
		print(data)
	s.close()

sendingMsg()
gettingMsg()