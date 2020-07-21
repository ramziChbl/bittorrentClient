import socket, bencode
from bitarray import bitarray

class Peer():
	"""docstring for Peer"""
	def __init__(self, ip, port):
		super(Peer,).__init__()
		self.ip = ip
		self.port = port
		self.sentHandshake = False
		self.receivedBitfield = False
		self.sentUnchoke = False

	def saveBitfield(self, bitfield):
		self.pieces = bitarray()
		self.pieces.frombytes(bitfield)
		

	def describePeer(self):
		print('{} : {} -> {}...'.format(self.ip, self.port, self.pieces[:10]))


	

