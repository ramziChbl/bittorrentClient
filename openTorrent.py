import asyncio, bencode
from torrentFile import TorrentFile
from tracker import Tracker
from client import Client
import socket

client = Client()
'''
seedsTorrent = TorrentFile('torrents/file2.torrent')
seedsTorrent.describe()

print(seedsTorrent.getSize())
'''
centosTorrent = TorrentFile('torrents/CentOS-8.1.1911-x86_64-boot.torrent')
centosTorrent.describe()

centosTracker = Tracker(centosTorrent)
centosTracker.describe()
'''
epubTorrent = TorrentFile('torrents/Jean-Christophe Grangé - Le Jour des cendres.epub.torrent')
epubTorrent.describe()

epubTracker = Tracker(epubTorrent.announce)
epubTracker.connect(epubTorrent, client)
print()

epubTracker.describe()
epubTracker.createNmapCommands()
'''