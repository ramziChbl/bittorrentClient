import socket, bencode
from bitarray import bitarray

class Peer():
	"""docstring for Peer"""
	def __init__(self, ip, port, idHash):
		super(Peer,).__init__()
		self.ip = ip
		self.port = port
		self.id = idHash
		self.sentHandshake = False
		self.receivedBitfield = False
		self.sentUnchoke = False

	def saveBitfield(self, bitfield):
		self.pieces = bitarray()
		self.pieces.frombytes(bitfield) # Bitfield corresponding to pieces that the peer has
		

	def describePeer(self):
		if hasattr(self, 'pieces'):
			print('{} : {} -> {}...'.format(self.ip, self.port, self.pieces[:10]))
		else:
			print('{} : {}'.format(self.ip, self.port))



	

