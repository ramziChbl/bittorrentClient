import requests, bencode

class Tracker():
	"""docstring for Tracker"""
	def __init__(self, url):
		self.url = url
		self.peers = {}


	def connect(self, torrent, myClient):
		content = self.requestToTracker(torrent, myClient)
		decodedContent = bencode.decode(content)

		requiredKeys = ['interval', 'peers']
		# check if tracker repsonse includes all required keys
		assert  all(elem in decodedContent.keys()  for elem in requiredKeys), "Tracker response error : missing keys"

		# Set attributes from decodedContent dictionary
		for k,v in decodedContent.items():
			if k == 'peers':
				if isinstance(v, list):
					setattr(self, k, v)
				else:
					decodedPeers = self.extractEncodedPeers(v)
					setattr(self, k, decodedPeers)
			else:
				setattr(self, k, v)


	def extractEncodedPeers(self, byteString):
		peer = {}
		peers = []
		i = 0
		while i<len(byteString):
			peer = {}
			peer['ip'] = str(byteString[i]) + '.' + str(byteString[i+1]) + '.' + str(byteString[i+2]) + '.' + str(byteString[i+3])
			peer['port'] = byteString[i+4] * 255 + byteString[i+5]
			peers.append(peer)
			i += 6
		return peers

	def requestToTracker(self, torrent, myClient):
		getParameters = {
			'info_hash' : torrent.infoHash,
			'peer_id' : myClient.peerId,
			'port' : myClient.port,
			'uploaded' : torrent.uploaded,
			'downloaded' : torrent.downloaded,
			'left' : torrent.left
		}

		response = requests.get(
    		self.url,
    		params=getParameters,
		)
		if response:
			return response.content
		else:
			return

	def describe(self):
		attributes = vars(self)
		print('Tracker Keys :', end='')
		for key in attributes:
			print(key, end=', ')
		print()


	