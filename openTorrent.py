import asyncio, bencode, pprint

pp = pprint.PrettyPrinter()

torrent = bencode.bread('file2.torrent')
print(torrent.keys())
print(torrent['announce'])
print(torrent['announce-list'])
print(torrent['comment'])
print(torrent['info']['name'])
print(torrent['info']['length'])
print(torrent['info']['piece length'])

#print(torrent['info'].keys())
#pp.pprint(bencode.bread('file.torrent')['announce'])