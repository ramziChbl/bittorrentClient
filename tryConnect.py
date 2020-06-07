import socket, bencode

handshakeMessage = b'\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00{\xcb\xc3B\xefF\x8f\x05\xb4\x07\x1f[\xc3\x0b;j\xa2.\xe3chellohellohellohello'
handshakeMessage = b'\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00\xc4O\x93\x1b\x1a9\x86\x85\x12B\xd7U\xd0\xacF\xe9\xfa<]2hellohellohellohello'
#TCP_IP = '185.45.195.174'
#TCP_PORT = 20129

BUFFER_SIZE = 69

TCP_IP = '67.241.66.89'
TCP_IP = '172.220.86.135'
TCP_PORT = 51413
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.socket()
s.connect((TCP_IP, TCP_PORT))
print('connected')
s.send(handshakeMessage)
print('send')
data = s.recv(BUFFER_SIZE)
print('recv')
s.close()
print('close')
 
print("received data:" + str(data))