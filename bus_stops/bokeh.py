import pygal
from pygal.style import BlueStyle
import MySQLdb as mysql

db = mysql.connect(host='127.0.0.1',
				   user='root',
				   passwd='TusuZ0Sx',
				   db="routes")
				   
cur = db.cursor()

query = "SELECT routes, count(routes) as num from routes group by routes order by num asc LIMIT 5"

cur.execute(query)
stuff = cur.fetchall()

bus_names = []
bus_routes = []
for bus in stuff:
	bus_names.append(bus[0])
	bus_routes.append(int(bus[1]))
	
print len(bus_names)
print len(bus_routes)

bar_chart = pygal.Bar(y_title='Number of Stops', x_title='Bus Route Name', show_legend=False, width=1200, x_label_rotation=90, label_font_size=8, style=BlueStyle)
bar_chart.title = 'Number of Stops Per Route'
bar_chart.x_labels = bus_names
bar_chart.add('stops', bus_routes)  # Add some values
bar_chart.render_to_file('stops.svg')  # Save the svg to a file
