import socket, bencode, struct
from peer import Peer
messageType = {
	0 : 'choke',
	1 : 'unchoke',
	2 : 'interested',
	3 : 'notinterested',
	4 : 'have',
	5 : 'bitfield',
	6 : 'request',
	7 : 'piece',
	8 : 'cancel'
}

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
	# length contains id size so i substracted it to get real payload size
	messageDict = {
		'length' : int.from_bytes(message[:4], byteorder='big') - 1,
		'id' : message[4]
	}


	messageDict['payload'] = message[5:messageDict['length'] + 5]
	#if messageDict['payload'] == b'':

	if messageType == 5: # Bitfield
		pass

		
	return messageDict


handshakeMessage = b'\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00\xc4O\x93\x1b\x1a9\x86\x85\x12B\xd7U\xd0\xacF\xe9\xfa<]2hellohellohellohello'

HANDSHAKE_SIZE = 68

TCP_IP = '158.69.55.241'
TCP_IP = '5.79.77.65'
#TCP_PORT = 51413
TCP_PORT = 50670

peer = Peer('5.79.77.65', 50670)
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((peer.ip, peer.port))
#s.connect((TCP_IP, TCP_PORT))
print('Connected')

s.send(handshakeMessage)
print('Handshake sent')

data = s.recv(HANDSHAKE_SIZE)
print(data)
print(len(data))
print('Received data')

message = s.recv(512)
print('Received message')
print(message)
msgDict = parseMessage(message)

payload = s.recv(msgDict['length'])
print('Received payload')
#print(payload)
#print(len(payload))
msgDict['payload'] = payload
print(msgDict)

peer.saveBitfield(msgDict['payload'])

peer.describePeer()
'''

unchokeMsg = b'\x00\x00\x00\x01\x02'
print('Sending interested message')
s.send(unchokeMsg)
message = s.recv(512)
print(message)

requestMsg = b'\x00\x00\x00\x0D\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80'
print('Sending request message')
s.send(requestMsg)

print('Waiting for reply')
message = s.recv(512)
print(message)


#print('Received message')
#print(message)

 
#print("Received data:")
#print(parseHandshake(data))

#print('Received message')
#print(message)
#print(parseMessage(message))

s.close()
print('Connection closed')
'''