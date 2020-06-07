import asyncio, bencode
from torrentFile import TorrentFile
from tracker import Tracker
from client import Client
import socket

client = Client()
seedsTorrent = TorrentFile('torrents/file2.torrent')
seedsTorrent.describe()

seedsTracker = Tracker(seedsTorrent.announce)
seedsTracker.connect(seedsTorrent, client)
print()

seedsTracker.describe()

infoHash = seedsTorrent.infoHash
#byte = "BitTorrent protocol\0\0\0\0\0\0\0\0".encode()
#print(byte)
handshakeMessage = str(19).encode() + "BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00".encode() + infoHash + client.peerId.encode()
print(handshakeMessage)
print(len(handshakeMessage))
peers = seedsTracker.peers

for peer in peers:
	print("nmap -p {} {}".format( peer['port'], peer['ip']))

"""
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

peers = centosTracker.peers
print('-----> {} peers'.format(len(peers)))
peer = peers[0]
print(peer)
#reader, writer = asyncio.open_connection(peer['ip'], peer['port'])
print(type(tf.infoHash))
infoHash = tf.infoHash
#byte = "BitTorrent protocol\0\0\0\0\0\0\0\0".encode()
#print(byte)
handshakeMessage = str(19).encode() + "BitTorrent protocol\x00\x00\x00\x00\x00\x00\x00\x00".encode() + tf.infoHash + client.peerId.encode()
print(handshakeMessage)
print(len(handshakeMessage))

#for peer in peers:
#	print("nmap -p {} {}".format( peer['port'], peer['ip']))


#TCP_IP = peer['ip']
TCP_IP = '195.178.197.57'
#TCP_PORT = peer['port']
TCP_PORT = 64611
BUFFER_SIZE = 69
MESSAGE = "Hello, World!"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#socket.socket()
s.connect((TCP_IP, TCP_PORT))
s.send(handshakeMessage)
data = s.recv(BUFFER_SIZE)
s.close()
 
print("received data:" + data)
"""