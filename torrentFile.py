import bencode, pprint

class TorrentFile():
	"""docstring for torrentFile"""
	def __init__(self, filePath):
		self.filePath = filePath
		decodedDict = bencode.bread(filePath)
		dictKeys = decodedDict.keys()
		
		if 'announce' in dictKeys:
			#print('  announce = ' + decodedDict['announce'])
			self.announce = decodedDict['announce']

		if 'announce-list' in dictKeys:
			#print('  announce-list = ' + str(decodedDict['announce-list']))
			self.announceList = decodedDict['announce-list']

		if 'creation date' in dictKeys:
			#print('  creation date = ' + str(decodedDict['creation date']))
			self.creationDate = decodedDict['creation date']

		if 'created by' in dictKeys:
			#print('  created by = ' + decodedDict['created by'])
			self.createdBy = decodedDict['created by']

		if 'comment' in dictKeys:
			#print('  comment = ' + decodedDict['comment'])
			self.comment = decodedDict['comment']


		if 'info' in dictKeys:
			self.info = decodedDict['info']
			#self.name = decodedDict['info']['name']
			#self.pieceLength = decodedDict['info']['piece length']
			#self.pieces = decodedDict['info']['pieces']
			if 'files' in self.info.keys():
				self.multiFile = True
				#self.files = decodedDict['info']['files']
				
			else:
				self.multiFile = False
				#self.length = decodedDict['info']['length']

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
