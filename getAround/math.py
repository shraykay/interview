import re

def removeval(list, x):
   return [value for value in list if value != x]

line = '5*6/3+1'
regex = '(\*|\/|\+|\-)'
store = re.split(regex, line)

for x in range(len(store)):
	if '.' in store[x]:
		store[x] = float(store[x])
	elif store[x].isdigit():
		store[x] = int(store[x])
		
print store

def div(stores):
	for x in range(len(stores)):
		if stores[x] == '/':
			y = x-1
			z = x+1
			
			if isinstance(stores[y], float) or isinstance(stores[z], float):
				stores[x] = float(stores[y]) / float(stores[z])
			else:
				stores[x] = stores[y] / stores[z]
				
			del stores[z]
			del stores[y]	
			
			return stores

def mult(stores):
	for x in range(len(stores)):
		if stores[x] == '*':
			y = x-1
			z = x+1
			
			if isinstance(stores[y], float) or isinstance(stores[z], float):
				stores[x] = float(stores[y]) * float(stores[z])
			else:
				stores[x] = stores[y] * stores[z]
				
			del stores[z]
			del stores[y]	
			
			return stores	

def sub(stores):
	for x in range(len(stores)):
		if stores[x] == '-':
			y = x-1
			z = x+1
			
			if isinstance(stores[y], float) or isinstance(stores[z], float):
				stores[x] = float(stores[y]) - float(stores[z])
			else:
				stores[x] = stores[y] - stores[z]
				
			del stores[z]
			del stores[y]	
			
			return stores	
			
def add(stores):
	for x in range(len(stores)):
		if stores[x] == '+':
			y = x-1
			z = x+1
			
			if isinstance(stores[y], float) or isinstance(stores[z], float):
				stores[x] = float(stores[y]) + float(stores[z])
			else:
				stores[x] = stores[y] + stores[z]
				
			del stores[z]
			del stores[y]	
			
			return stores	
			
while '/' in store:
	store = div(store)
while '*' in store:
	store = mult(store)
while '-' in store:
	store = sub(store)
while '+' in store:
	store = add(store)

print store[0]

	#store = removeval(store,'xxx')

#print store[0]
