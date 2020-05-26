import asyncio
from torrentFile import TorrentFile
from tracker import Tracker
from client import Client

client = Client()

tf2 = TorrentFile('torrents/file2.torrent')
tf2.describe()

ubuntuTracker = Tracker(tf2.announce)
ubuntuTracker.connect(tf2, client)
print()

tf = TorrentFile('torrents/CentOS-8.1.1911-x86_64-boot.torrent')
tf.describe()

centosTracker = Tracker(tf.announce)
centosTracker.connect(tf, client)

ubuntuTracker.describe()
print()
centosTracker.describe()
