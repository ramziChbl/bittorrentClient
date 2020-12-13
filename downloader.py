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

	def extractConnectedPeers(self):
		for peer in self.peers:
			self.sendHello(peer)

	def sendHello(self, peer):
		#handshakeMessage = self.torrentInfo.infoHash
		handshakeMessage = b'\x13BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00' + self.torrentInfo.infoHash + b'hellohellohellohello'

		HANDSHAKE_SIZE = 68
		print('trying {}:{}'.format(peer.ip, peer.port)) 
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((peer.ip, peer.port))
		#print('{}:{} is connected'.format(peer.ip, peer.port))
		print(' sending Handshake')
		s.send(handshakeMessage)
		print(' Handshake sent')
		print(' Waiting for reply')
		data = s.recv(HANDSHAKE_SIZE)
		#print(data)
		#print(len(data))
		#print('Received data')
		receivedHandshake = self.parseHandshake(data)
		pprint.pprint(receivedHandshake)
		#print(receivedHandshake)


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


		


		