import bencode, pprint, hashlib

class TorrentFile():
	"""docstring for torrentFile"""
	# announce (required) : The announce URL of the tracker (string)
	# announce-list : (optional) this is an extention to the official specification, offering backwards-compatibility. (list of lists of strings)
	# createdBy : (optional) name and version of the program used to create the .torrent (string)
	# creationDate : (optional) the creation time of the torrent, in standard UNIX epoch format
	# comment : (optional) free-form textual comments of the author (string)
	# info (required) : a dictionary that describes the file(s) of the torrent.
	# (self added) infoHash
	# fileSize
	# left
	# downloaded
	# uploaded

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
			print(self.info.keys())
			hashObj = hashlib.sha1(bencode.encode(self.info))
			self.infoHash = hashObj.digest()

			if 'files' in self.info.keys():
				self.multiFile = True
				
			else:
				self.multiFile = False

		self.fileSize = self.calculateSize()
		self.left = self.fileSize
		self.downloaded = 0
		self.uploaded = 0

	def calculateSize(self):
		if(self.multiFile):
			l = 0
			for file in self.info['files']:
				l += file['length']
			return l
		else:
			return self.info['length']

	def describe(self):
		attributes = vars(self)
		print('Metainfo Keys :', end='')
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
			print('    pieces number = ' + str(len(attributes['info']['pieces']) // 20))
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
			else:
				print('    Single-file')
				print('    length = ' + str(attributes['info']['length']))
		pass

