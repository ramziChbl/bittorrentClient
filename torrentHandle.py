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
		trackerList
		currentTracker
		currentTrackerIndex (0 for announce and 1.. for announce list)
	'''
	def __init__(self, torrentFilePath, client):
		self.client = client
		self.torrentInfo = TorrentFile(torrentFilePath)
		self.extractTrackers()

		# Remove udp trackers from list
		self.filterTrackersByProtocol('udp')

		self.currentTrackerIndex = 0
		self.currentTracker = Tracker(self.trackerList[self.currentTrackerIndex])
		

	def connectToTracker(self):
		self.currentTracker.connect(self.torrentInfo, self.client)

	def describeTorrent(self):
		self.torrentInfo.describe()

	def describeTracker(self):
		self.currentTracker.describe()

	def printAllTrackers(self):

		print(self.trackerList)
		print(len(self.trackerList))

	def extractTrackers(self):
		self.trackerList = []
		self.trackerList.append(self.torrentInfo.announce)
		for trackerEntry in self.torrentInfo.announceList:
			self.trackerList.append(trackerEntry[0])

	def filterTrackersByProtocol(self, protocol='udp'):
		protocolLength = len(protocol)
		self.trackerList = [x for x in self.trackerList if x[:protocolLength] != protocol]
