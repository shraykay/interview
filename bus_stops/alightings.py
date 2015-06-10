import pygal
from pygal.style import BlueStyle
import MySQLdb as mysql

db = mysql.connect(host='127.0.0.1',
				   user='root',
				   passwd='TusuZ0Sx',
				   db="routes")
				   
cur = db.cursor()

query = "select routes, count(routes), round(sum(alightings),1) as alite from routes group by routes order by alite asc"

cur.execute(query)
stuff = cur.fetchall()
#print stuff

bus_names = []
bus_routes = []
bus_boardings = []

for bus in stuff:
	bus_names.append(bus[0])
	bus_routes.append(int(bus[1]))
	bus_boardings.append(bus[2])
	
print len(bus_names)
print len(bus_routes)
print len(bus_boardings)

line_chart = pygal.Line(y_title='Number of Alightings', x_title='Bus Route Name', show_legend=False, width=1200, x_label_rotation=90, label_font_size=8, style=BlueStyle)
line_chart.title = 'Total Alightings per Month'
line_chart.x_labels = bus_names
line_chart.add('boardings', bus_boardings)
line_chart.render_to_file('alightings.svg')