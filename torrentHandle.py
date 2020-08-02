import asyncio, bencode
from torrentFile import TorrentFile
from tracker import Tracker
from client import Client
import socket

class TorrentHandle():
	"""docstring for TorrentHandle"""
	'''
	ARGS:
		client
		torrentInfo
		currentTracker
		currentTrackerIndex (0 for announce and 1.. for announce list)
	'''
	def __init__(self, torrentFilePath, client):
		self.client = client
		self.torrentInfo = TorrentFile(torrentFilePath)
		self.currentTrackerIndex = 0
		self.currentTracker = Tracker(self.torrentInfo)

	def getPeersFromTracker(self):
		self.currentTracker.connect(self.torrentInfo, self.client)

	def describeTorrent(self):
		self.torrentInfo.describe()

	def describeTracker(self):
		self.currentTracker.describe()






		
		