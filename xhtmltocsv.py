#Afreen hameed 
#converts stock xhtml to csv format

import sys
import xml.dom.minidom
document = xml.dom.minidom.parse(sys.argv[1])
tableElements = document.getElementsByTagName('table')

print('exchange,symbol,company,volume,price,change')
helper1=1
helper=1
for tr in tableElements[2].getElementsByTagName('tr'):
	data = []
	if helper==1: #executes once for header
		helper=0

		for td in tr.getElementsByTagName('td'):
			for node in td.childNodes:
					if node.nodeType == node.TEXT_NODE:
							continue

	else:
		for td in tr.getElementsByTagName('td'):
			for a in td.getElementsByTagName('a'):
				for node in a.childNodes:
						if node.nodeType == node.TEXT_NODE:
							data.append(node.nodeValue)
		data[0]=data[0].rstrip()
		temp=data[0].split('(')
		data[0]=(temp[1])[:-1]
		data.append(temp[0])
		for td in tr.getElementsByTagName('td'):
			for node in td.childNodes:
					if node.nodeType == node.TEXT_NODE:
							data.append(node.nodeValue)
		del data[2]
		del data[2]
		del data[2]
		del data[5]
		if helper1:
			helper1=0
			data[3]=(data[3])[1:]

		print('Nasdaq,'+','.join(data))