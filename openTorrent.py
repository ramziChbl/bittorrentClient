import asyncio, bencode
from torrentFile import TorrentFile
from tracker import Tracker
from client import Client
from torrentHandle import TorrentHandle
import socket

client = Client()
centosTorrent = TorrentHandle('torrents/CentOS-8.1.1911-x86_64-boot.torrent', client)
centosTorrent.describeTorrent()
centosTorrent.getPeersFromTracker()
centosTorrent.describeTracker()
