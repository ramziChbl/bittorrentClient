import socket, bencode


def parseHandshake(data):
	handshakeDict = {
		'pstrlen' : data[0],
	}

	handshakeDict['pstr'] = data[1:handshakeDict['pstrlen']+1]

	data = data[handshakeDict['pstrlen']+1:]
	handshakeDict['reserved'] = data[:8]
	data = data[8:]
	handshakeDict['info_hash'] = data[:20]
	handshakeDict['peer_id'] = data[20:]
	return handshakeDict

#handshakeMessage = b'\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00{\xcb\xc3B\xefF\x8f\x05\xb4\x07\x1f[\xc3\x0b;j\xa2.\xe3chellohellohellohello'
handshakeMessage = b'\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00\xc4O\x93\x1b\x1a9\x86\x85\x12B\xd7U\xd0\xacF\xe9\xfa<]2hellohellohellohello'

BUFFER_SIZE = 69

TCP_IP = '67.241.66.89'
TCP_IP = '172.220.86.135'
TCP_IP = '50.38.32.181'
TCP_PORT = 51413
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.socket()
s.connect((TCP_IP, TCP_PORT))
print('Connected')
s.send(handshakeMessage)
print('Handshake sent')
data = s.recv(BUFFER_SIZE)
print('Received data')
s.close()
print('Connection closed')
 
print("Received data:" + str(data))
print(type(data))
print(len(data))
print(parseHandshake(data))


