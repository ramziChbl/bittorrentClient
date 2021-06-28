from client import Client
from torrentHandle import TorrentHandle
from downloader import Downloader

client = Client()

ubuntuTorrent = TorrentHandle('torrents/ubuntu-20.10-live-server-amd64.iso.torrent', client)
ubuntuTorrent.describeTorrent()
ubuntuTorrent.switchToNextTracker()
ubuntuTorrent.connectToTracker()
ubuntuTorrent.describeTracker()

ubuntuDownloader = Downloader(ubuntuTorrent.torrentInfo, ubuntuTorrent.currentTracker.peers)
#ubuntuDownloader.extractConnectedPeers()
