import socket, bencode, struct

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

def parseMessage(message):
	messageDict = {
		'length' : int.from_bytes(message[:4], byteorder='big'),
		'id' : message[4]
	}

	messageDict['payload'] = message[5:messageDict['length'] - 1]
	return messageDict


handshakeMessage = b'\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00\xc4O\x93\x1b\x1a9\x86\x85\x12B\xd7U\xd0\xacF\xe9\xfa<]2hellohellohellohello'

BUFFER_SIZE = 69

#TCP_IP = '67.241.66.89'
#TCP_IP = '172.220.86.135'
TCP_IP = '50.38.32.181'
TCP_PORT = 51413
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((TCP_IP, TCP_PORT))
print('Connected')
s.send(handshakeMessage)
print('Handshake sent')
data = s.recv(BUFFER_SIZE)
print('Received data')
message = s.recv(256)
print('Received message')


s.close()
print('Connection closed')
 
print("Received data:")
print(parseHandshake(data))

print('Received message')
print(message)
print(parseMessage(message))

