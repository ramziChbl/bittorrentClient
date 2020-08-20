from client import Client
from torrentHandle import TorrentHandle

client = Client()
'''
centosTorrent = TorrentHandle('torrents/CentOS-8.1.1911-x86_64-boot.torrent', client)
centosTorrent.describeTorrent()
centosTorrent.connectToTracker()
centosTorrent.describeTracker()
centosTorrent.currentTracker.createNmapCommands()
'''

kingTorrent = TorrentHandle('torrents/kingBook.torrent', client)
kingTorrent.describeTorrent()

#kingTorrent.printAllTrackers()
kingTorrent.connectToTracker()
kingTorrent.describeTracker()

