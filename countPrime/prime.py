initial = 3
final = 1000
count = 1 #counting 2 already

while initial < final:
	bool = True
	for x in range(3,initial,2):
		if initial % 2 == 0:
			bool = False
			break
		if initial % x == 0:
			bool = False
			break
	if bool == True:
		print "success on initial: %s" % (initial)
		count += 1
	initial += 1

print count

