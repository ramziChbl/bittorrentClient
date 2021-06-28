import socket
import pprint

class Downloader():
	"""docstring for Downloader"""
	# torrentInfo
	# connectedPeers
	# pieces ?bitarray?
	def __init__(self, torrentFile, peers):
		self.torrentInfo = torrentFile
		self.peers = peers
		self.connectedPeers = self.extractConnectedPeers()
		print('Connected Peers list :')
		for p in self.connectedPeers:
			print(p)

	def extractConnectedPeers(self):
		print('{} peers'.format(len(self.peers)))
		connectedPeers = []
		i = 0
		for peer in self.peers:
			i += 1
			print(i)
			if(self.sendHello(peer)):
				connectedPeers.append(peer)
		return connectedPeers

	def sendHello(self, peer):
		#handshakeMessage = self.torrentInfo.infoHash
		handshakeMessage = b'\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00' + self.torrentInfo.infoHash + b'hellohellohellohello'

		HANDSHAKE_SIZE = 68
		print('trying {}:{}'.format(peer.ip, peer.port)) 
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.settimeout(2)
			try:
				s.connect((peer.ip, peer.port))
			except socket.timeout as e:
				print('yoo timeout')
				return False
			else:
				#print('{}:{} is connected'.format(peer.ip, peer.port))
				#print(' sending Handshake')
				s.send(handshakeMessage)
				#print(' Handshake sent')
				#print(' Waiting for reply')
				try:
					data = s.recv(HANDSHAKE_SIZE)
				except s.timeout as e:
					return False

				if not data:
					return False
				#print(data)
				#print(len(data))
				#print('Received data')
				#print(' Received reply')
				receivedHandshake = self.parseHandshake(data)
				pprint.pprint(receivedHandshake)
				#print(receivedHandshake)
				return True

	def parseHandshake(self, data):
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
