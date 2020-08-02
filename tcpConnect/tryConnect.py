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

'''
handshakeMessage = b'\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00\xc4O\x93\x1b\x1a9\x86\x85\x12B\xd7U\xd0\xacF\xe9\xfa<]2hellohellohellohello'
'''
infoHash = b"@\xd6\x02/y\x9e\x9d\xe2'\xd9\xc0\xb5\n\x08O\xe7\xd0\x06\xd6\xfd"

handshakeMessage = b'\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00' + infoHash + b'hellohellohellohello'


HANDSHAKE_SIZE = 68

TCP_IP = '206.217.129.233'
TCP_PORT = 6881

peer = Peer(TCP_IP, TCP_PORT)
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((peer.ip, peer.port))

print('Connected')

s.send(handshakeMessage)
print('Handshake sent')

data = s.recv(HANDSHAKE_SIZE)
print(data)
print(len(data))
print('Received data')

message = s.recv(5) # receive length (4 bytes) + id (1 byte)
print('Received message')
print(message)
msgDict = parseMessage(message)

if msgDict['id'] == 5: # received bitfield message
	payload = s.recv(msgDict['length'])
	print('Received payload')
	#print(payload)
	print(len(payload))
	msgDict['payload'] = payload
	print(msgDict)

	peer.saveBitfield(msgDict['payload'])

peer.describePeer()

# Send interested message
#interested: <len=0001(4 bytes)><id=2(1 bytes)>
interrestedMsg = b'\x00\x00\x00\x01\x02'
print('Sending interested message')
s.send(interrestedMsg)

print('Waiting for reply')
message = s.recv(128)
print(message)




# Send request for first piece
#request: <len=0013><id=6><index(4 bytes)><begin(4 bytes)><length(4 bytes)>
requestMsg = b'\x00\x00\x00\x0D\x06\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x80\x00'
print('Sending request message')
s.send(requestMsg)

print('Waiting for reply')
#message = s.recv(32768)
data = 0
n = 32768
while data < n:
	packet = s.recv(1024)
	print(packet)
	if not packet:
		print('Nada')
		break
	data += len(packet)
	print(data)

s.close()
print('Connection closed')
#print(message)