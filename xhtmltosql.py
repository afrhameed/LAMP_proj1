#Afreen hameed 
#loads stock xhtml to mysql table
import mysql.connector
import sys
import xml.dom.minidom


document = xml.dom.minidom.parse(sys.argv[1])
tableElements = document.getElementsByTagName('table')

helper1=1
helper=1
n=0
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
		
		try:
		    cnx = mysql.connector.connect(host='localhost', user='root', password='Divastar1998', database='demo')
		    cursor = cnx.cursor()
		    idstr=data[0]+(sys.argv[1])[13:-6]
		    query = 'INSERT INTO stocks(exchange,symbol,company,volume,price,changee,idsym) VALUES (%s,%s,%s,%s,%s,%s,%s)'
		    cursor.execute(query, ('Nasdaq',data[0],data[1],float(data[2].replace(',','')),float(data[3].replace(',','')),float(data[4].replace(',','')),idstr))
  		    cnx.commit()
		    cursor.close()
		except mysql.connector.Error as err:
		    print(err)
		finally:
		    try:
		        cnx
		    except NameError:
		        pass
		    else:
		        cnx.close()