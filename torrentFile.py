import bencode, pprint, hashlib

class TorrentFile():
	"""docstring for torrentFile"""
	def __init__(self, filePath):
		self.filePath = filePath

		decodedDict = bencode.bread(filePath)
		dictKeys = decodedDict.keys()
		requiredKeys = ['announce', 'info']

		# check if torrent file includes all required keys
		assert  all(elem in dictKeys  for elem in requiredKeys), "Torrent File required key missing"
		
		if 'announce' in dictKeys:
			self.announce = decodedDict['announce']

		if 'announce-list' in dictKeys:
			self.announceList = decodedDict['announce-list']

		if 'creation date' in dictKeys:
			self.creationDate = decodedDict['creation date']

		if 'created by' in dictKeys:
			self.createdBy = decodedDict['created by']

		if 'comment' in dictKeys:
			self.comment = decodedDict['comment']


		if 'info' in dictKeys:
			self.info = decodedDict['info']
			hashObj = hashlib.sha1(bencode.encode(self.info))
			self.infoHash = hashObj.digest()

			if 'files' in self.info.keys():
				self.multiFile = True
				
			else:
				self.multiFile = False

	def describe(self):
		attributes = vars(self)
		print('Keys :', end='')
		for key in attributes:
			print(key, end=', ')
		print()

		dictKeys = attributes.keys()
		
		if 'announce' in dictKeys:
			print('  announce = ' + attributes['announce'])

		if 'announceList' in dictKeys:
			print('  announce-list = ' + str(attributes['announceList']))

		if 'creationDate' in dictKeys:
			print('  creation date = ' + str(attributes['creationDate']))

		if 'createdBy' in dictKeys:
			print('  created by = ' + attributes['createdBy'])

		if 'comment' in dictKeys:
			print('  comment = ' + attributes['comment'])

		if 'infoHash' in dictKeys:
			print('  hash = ' + str(attributes['infoHash']))

		if 'info' in dictKeys:
			print('  info : ', end='')
			for key in  attributes['info'].keys():
				print(key, end=', ')
			print()

			print('    name = ' + attributes['info']['name'])
			print('    piece length = ' + str(attributes['info']['piece length']))
			print('    pieces number = ' + str(len(attributes['info']['pieces'])))
			if self.multiFile:
				print('    Multi-file')
				print('    Files :')
				for file in attributes['info']['files']:
					print('        length = ' + str(file['length']))
					delimiter = '/'
					path = delimiter.join(file['path'])
					print('        path = ' + path)
					print()
				
				pp = pprint.PrettyPrinter()
				#pp.pprint(attributes['info']['files'])
			else:
				print('    Single-file')
				print('    length = ' + str(attributes['info']['length']))
				#pp = pprint.PrettyPrinter()
				#pp.pprint(attributes['info']['pieces'])
		pass
