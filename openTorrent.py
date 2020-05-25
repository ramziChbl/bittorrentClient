import asyncio, bencode, pprint, json, requests, hashlib
from torrentFile import TorrentFile


def extractPeers(byteString):
	peer = {}
	peers = []
	i = 0
	while i<len(byteString):
		peer = {}
		peer['ip'] = str(byteString[i]) + '.' + str(byteString[i+1]) + '.' + str(byteString[i+2]) + '.' + str(byteString[i+3])
		peer['port'] = byteString[i+4] * 255 + byteString[i+5]
		peers.append(peer)
		i += 6
	return peers


tf2 = TorrentFile('torrents/file2.torrent')
#tf2.describe()


tf = TorrentFile('torrents/CentOS-8.1.1911-x86_64-boot.torrent')
#tf.describe()
getParameters = {
	'info_hash' : tf2.infoHash,
	'peer_id' : 'hellohellohellohello',
	'port' : '8992',
	'uploaded' : '0',
	'downloaded' : '0',
	'left' : tf2.info['length']# str(metainfo['info']['length'])
}

#print(getParameters)

response = requests.get(
    tf2.announce,
    params=getParameters,
)

#print(response)
print(response.url)
decodedContent = bencode.decode(response.content)
print(decodedContent)
print(type(decodedContent['peers']))
#pp = pprint.PrettyPrinter()
#pp.pprint(decodedContent)

getParameters['info_hash'] = tf.infoHash
l = 0
for f in tf.info['files']:
	l += f['length']

getParameters['left'] = l
response = requests.get(tf.announce, params = getParameters)

print()
#print(response)
print(response.url)
#print(response.content)
decodedContent = bencode.decode(response.content)
print(decodedContent)
print(type(decodedContent['peers']))
if isinstance(decodedContent['peers'], bytes):
	peers = extractPeers(decodedContent['peers'])
	print(peers)
#print(decodedContent['peers'])
