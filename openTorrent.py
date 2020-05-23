import asyncio, bencode, pprint, json

def describeTorrentDict(decodedDict):
	dictKeys = decodedDict.keys()
	print('Keys :', end='')
	for key in dictKeys:
		print(key, end=', ')
	print()
	
	if 'announce' in dictKeys:
		print('  announce = ' + decodedDict['announce'])

	if 'announce-list' in dictKeys:
		print('  announce-list = ' + str(decodedDict['announce-list']))

	if 'creation date' in dictKeys:
		print('  creation date = ' + str(decodedDict['creation date']))

	if 'created by' in dictKeys:
		print('  created by = ' + decodedDict['created by'])

	if 'comment' in dictKeys:
		print('  comment = ' + decodedDict['comment'])


	if 'info' in dictKeys:
		print('  info : ', end='')
		for key in  decodedDict['info'].keys():
			print(key, end=', ')
		print()

		print('    name = ' + decodedDict['info']['name'])
		print('    piece length = ' + str(decodedDict['info']['piece length']))
		print('    pieces number = ' + str(len(decodedDict['info']['pieces'])))
		if 'files' in decodedDict['info'].keys():
			print('    Multi-file')
			print('    Files :')
			for file in decodedDict['info']['files']:
				print('        length = ' + str(file['length']))
				delimiter = '/'
				path = delimiter.join(file['path'])
				print('        path = ' + path)
				print()
			
			pp = pprint.PrettyPrinter()
			#pp.pprint(decodedDict['info']['files'])
		else:
			print('    Single-file')
			print('    length = ' + str(decodedDict['info']['length']))
			#pp = pprint.PrettyPrinter()
			#pp.pprint(decodedDict['info']['pieces'])

	pass



def readTorrentFile(filePath):
	print('Reading file : ' + filePath)
	decodedDict = bencode.bread(filePath)
	describeTorrentDict(decodedDict)
	
	print()

#readTorrentFile('file.torrent')
readTorrentFile('file2.torrent')

'''
pp = pprint.PrettyPrinter()

torrent = bencode.bread('file2.torrent')
print(torrent.keys())
print(torrent['announce'])
print(torrent['announce-list'])
print(torrent['comment'])
print(torrent['info']['name'])
print(torrent['info']['length'])
print(torrent['info']['piece length'])
'''