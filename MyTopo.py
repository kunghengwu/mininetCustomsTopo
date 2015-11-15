from mininet.topo import Topo
import string
import sys

class MyTopo(Topo):
	def __init__(self,filename):
		"Create custom topo"
		#inistialize topology
		Topo.__init__(self)
		
		#get topodata from file
		try:
			topoFile  = open(filename,'r')
		except:
			print 'no this file'
			sys.exit(1)
		allLines = topoFile.readlines()
		print 'this is filename:',filename,allLines
		topoFile.close()
		hostList = []
		switchList = []
		linkerList = []
		for eachLine in allLines:
			eachLine = eachLine.strip()
			#i = i + 1
			if(eachLine != ''):
				if((eachLine[0] == 'h') & (eachLine.find(',')==-1)):
					for i in range(int(eachLine[1])) :
						hostList.append('h%d'%(i+1))
				elif ((eachLine[0] == 's') & (eachLine.find(',')==-1)):
					for i in range(int(eachLine[1])) :
						switchList.append('s%d'%(i+1))
				elif eachLine != '' :
					link = eachLine.split(',')
					linkerList.append(link)
	
		#add hosts and switches
		for switch in switchList:
			self.addSwitch(switch)
	
		for host in hostList:
			self.addHost(host)
	
		for linker in linkerList:
			self.addLink(linker[0],linker[1])
		#self.addLink('h1','s3')

topos = {'mytopo':MyTopo}
