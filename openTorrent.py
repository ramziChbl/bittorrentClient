import asyncio, bencode, pprint, json, requests, hashlib
from torrentFile import TorrentFile

tf2 = TorrentFile('file2.torrent')
tf2.describe()


tf = TorrentFile('file.torrent')
tf.describe()
"""

infohash = hashlib.sha1(bencode.encode(metainfo['info']))
hashstring = infohash.digest()

getParameters = {
	'info_hash' : hashstring,
	'peer_id' : 'hellohellohellohello',
	'port' : '8992',
	'uploaded' : '0',
	'downloaded' : '0',
	'left' : str(metainfo['info']['length'])
}

print(getParameters)

response = requests.get(
    'https://torrent.ubuntu.com/announce',
    params=getParameters,
)
print(response)
#print(response.content)
pp = pprint.PrettyPrinter()
pp.pprint(bencode.decode(response.content))
#print(bencode.decode(response.content))

"""