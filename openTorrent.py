from client import Client
from torrentHandle import TorrentHandle

client = Client()
'''
centosTorrent = TorrentHandle('torrents/CentOS-8.1.1911-x86_64-boot.torrent', client)
centosTorrent.describeTorrent()
centosTorrent.switchToNextTracker()
centosTorrent.connectToTracker()
centosTorrent.describeTracker()
centosTorrent.currentTracker.createNmapCommands()
'''

bunnyTorrent = TorrentHandle("torrents/VODO_Haphead_bundle.torrent", client)
bunnyTorrent.describeTorrent()

bunnyTorrent.printAllTrackers()
bunnyTorrent.connectToTracker()
#bunnyTorrent.describeTracker()
#kingTorrent.currentTracker.createNmapCommands()
