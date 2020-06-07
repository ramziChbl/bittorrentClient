import csv, subprocess, re, os

def peerToOutputs():
	with open('peersUbuntu.csv', 'r') as file: # File format : ip,port
		reader = csv.reader(file, delimiter=',')
		outputfileNumber = 1
		for row in reader:
			subprocess.run(['nmap', '-oG', 'output{:02}.txt'.format(outputfileNumber),'-p', row[1], row[0]])
			outputfileNumber += 1
	file.close()
	return outputfileNumber - 1

def outputsToOpen(outputfileNumber):
	openedPorts = open('openedPorts', 'w')
	for n in range(1, outputfileNumber+1):
		file = open('output{:02}.txt'.format(n))
		for line in file:
			reResult = re.search(r'((\d{1,3}\.){3}\d{1,3}).*Ports: (\d{4,})/open', line)
			if reResult:
				ip = reResult.group(1)
				port = reResult.group(3)
				print('{}:{}'.format(ip, port))
				openedPorts.write('{}:{}\n'.format(ip, port))
		file.close()
		os.remove('output{:02}.txt'.format(n))
	openedPorts.close()

outputsToOpen(50)



