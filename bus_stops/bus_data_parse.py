import csv
import MySQLdb as mysql

db = mysql.connect(host='127.0.0.1',
				   user='root',
				   passwd='TusuZ0Sx',
				   db="routes")

db.autocommit(True)
cur = db.cursor(mysql.cursors.DictCursor)

f = open('bus.csv')

for row in csv.reader(f):
	
	stop_id = row[0]
	on_street = row[1].strip()
	cross_street = row[2].replace('\"','\'')
	routes = row[3].strip()
	boardings = row[4].strip()
	alightings = row[5].strip()
	month_beginning = row[6].strip()
	daytype = row[7].strip()
	location = row[8].strip()
	
	if ',' in routes:
		
		if ',,' in routes:
			routes = routes.replace(",,",",")
			
		stops = routes.split(',')
		
		for stop in stops:
			stop = stop.strip()
			
			query = "INSERT INTO routes (stop_id, on_street, cross_street, routes, boardings, \
			alightings, month_beginning, daytype, location) VALUES (%s, \"%s\", \"%s\", \"%s\", %s, \
			%s, \"%s\", \"%s\", \"%s\")" % (stop_id, on_street, cross_street, stop, boardings, alightings, month_beginning, daytype, location)
			cur.execute(query)

	else:
		query = "INSERT INTO routes (stop_id, on_street, cross_street, routes, boardings, \
		alightings, month_beginning, daytype, location) VALUES (%s, \"%s\", \"%s\", \"%s\", %s, \
		%s, \"%s\", \"%s\", \"%s\")" % (stop_id, on_street, cross_street, routes, boardings, alightings, month_beginning, daytype, location)
		cur.execute(query)

	
#	if ',' in row[3]:
#		stops = row[3].split(',')
#		for stop in stops:
#			stop = stop.strip()
#			# print stop

